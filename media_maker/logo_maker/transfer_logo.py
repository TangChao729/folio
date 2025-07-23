#!/usr/bin/env python3
"""
SVG to App-Style Icon Converter

Usage: python transfer_logo.py input.svg
Output: input_logo.svg (app-style icon with background)

Features:
- Analyzes SVG colors to pick contrasting bright background
- Creates rounded app-style background
- Outputs 128x128 icon
- Supports both SVG and PNG output
"""

import sys
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
import colorsys
from typing import List, Tuple, Optional

class SVGAppIconConverter:
    def __init__(self):
        self.size = 128
        self.corner_radius = 16  # iOS-style rounded corners
        self.padding = 0  # Reduced padding for a larger icon

    def extract_colors_from_svg(self, svg_content: str) -> List[str]:
        """Extract color values from SVG content"""
        colors = []
        # Find fill colors
        fill_matches = re.findall(r'fill=["\']([^"\']+)["\']', svg_content)
        colors.extend(fill_matches)
        # Find stroke colors
        stroke_matches = re.findall(r'stroke=["\']([^"\']+)["\']', svg_content)
        colors.extend(stroke_matches)
        # Find style colors
        style_matches = re.findall(r'(?:fill|stroke):\s*([^;"\'\s]+)', svg_content)
        colors.extend(style_matches)
        # Filter out 'none', 'transparent', and currentColor
        valid_colors = []
        for color in colors:
            if color.lower() not in ['none', 'transparent', 'currentcolor']:
                valid_colors.append(color)
        return valid_colors

    def hex_to_rgb(self, hex_color: str) -> Optional[Tuple[int, int, int]]:
        """Convert hex color to RGB tuple"""
        try:
            hex_color = hex_color.strip('#')
            if len(hex_color) == 3:
                hex_color = ''.join([c*2 for c in hex_color])
            if len(hex_color) == 6:
                return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        except:
            pass
        return None

    def rgb_to_hex(self, rgb: Tuple[int, int, int]) -> str:
        """Convert RGB tuple to hex color"""
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

    def get_luminance(self, rgb: Tuple[int, int, int]) -> float:
        """Calculate the relative luminance of an RGB color (for contrast)"""
        r, g, b = [x / 255.0 for x in rgb]
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def contrast_ratio(self, rgb1: Tuple[int, int, int], rgb2: Tuple[int, int, int]) -> float:
        """Calculate the contrast ratio between two RGB colors"""
        lum1 = self.get_luminance(rgb1)
        lum2 = self.get_luminance(rgb2)
        lighter = max(lum1, lum2)
        darker = min(lum1, lum2)
        return (lighter + 0.05) / (darker + 0.05)

    def get_contrasting_color(self, colors: List[str]) -> str:
        """Choose the most contrasting bright background color from a palette"""
        palette = [
            '#ffffff',  # white
            '#f0f0f0',  # light grey
            '#e0f7fa',  # sky blue
            '#e3f2fd',  # light blue
            '#fffde7',  # light yellow
            '#fce4ec',  # light pink
            '#e8f5e9',  # light green
        ]
        palette_rgb = [self.hex_to_rgb(c) for c in palette]
        rgb_colors = []
        for color in colors:
            if color.startswith('#'):
                rgb = self.hex_to_rgb(color)
                if rgb:
                    rgb_colors.append(rgb)
        if not rgb_colors:
            rgb_colors = [(0, 0, 0)]
        avg_r = sum(rgb[0] for rgb in rgb_colors) / len(rgb_colors)
        avg_g = sum(rgb[1] for rgb in rgb_colors) / len(rgb_colors)
        avg_b = sum(rgb[2] for rgb in rgb_colors) / len(rgb_colors)
        avg_rgb = (int(avg_r), int(avg_g), int(avg_b))
        best_color = palette[0]
        best_contrast = 0
        for color, rgb in zip(palette, palette_rgb):
            if rgb is None:
                continue
            contrast = self.contrast_ratio(avg_rgb, rgb)
            if contrast > best_contrast:
                best_contrast = contrast
                best_color = color
        return best_color

    def create_gradient_background(self, base_color: str) -> str:
        # No gradient, just use the color directly
        return ""

    def process_svg_content(self, svg_content: str) -> Tuple[list, Tuple[float, float, float, float]]:
        """Process the original SVG to fit within the icon bounds and extract its child elements, normalizing viewBox to (0,0) if needed."""
        try:
            root = ET.fromstring(svg_content)
            original_width = None
            original_height = None
            viewbox = None
            if 'width' in root.attrib:
                try:
                    original_width = float(re.sub(r'[^\d.]', '', root.attrib['width']))
                except:
                    pass
                del root.attrib['width']
            if 'height' in root.attrib:
                try:
                    original_height = float(re.sub(r'[^\d.]', '', root.attrib['height']))
                except:
                    pass
                del root.attrib['height']
            if 'viewBox' in root.attrib:
                viewbox_str = root.attrib['viewBox']
                try:
                    viewbox = tuple(map(float, viewbox_str.split()))
                except:
                    viewbox = None
            if viewbox:
                vb_x, vb_y, vb_width, vb_height = viewbox
            elif original_width and original_height:
                vb_x, vb_y, vb_width, vb_height = 0, 0, original_width, original_height
                root.set('viewBox', f'0 0 {original_width} {original_height}')
            else:
                vb_x, vb_y, vb_width, vb_height = 0, 0, 24, 24
                root.set('viewBox', '0 0 24 24')
            children = list(root)
            children_strs = []
            # Always preserve <style> and all children
            if (vb_x != 0 or vb_y != 0):
                g = ET.Element('g')
                g.set('transform', f'translate({-vb_x}, {-vb_y})')
                for child in children:
                    g.append(child)
                children_strs.append(ET.tostring(g, encoding='unicode'))
            else:
                children_strs = [ET.tostring(child, encoding='unicode') for child in children]
            return children_strs, (0, 0, vb_width, vb_height)
        except Exception as e:
            print(f"Warning: SVG parsing failed ({e}), using fallback")
            return [svg_content], (0, 0, 24, 24)

    def convert_svg_to_app_icon(self, svg_path: str, output_format: str = 'svg') -> str:
        """Convert SVG to app-style icon"""
        try:
            with open(svg_path, 'r', encoding='utf-8') as f:
                svg_content = f.read()
            colors = self.extract_colors_from_svg(svg_content)
            print(f"Found colors: {colors}")
            bg_color = self.get_contrasting_color(colors)
            print(f"Generated background color: {bg_color}")
            children_strs, (vb_x, vb_y, vb_width, vb_height) = self.process_svg_content(svg_content)
            print(f"Original SVG viewBox: {vb_x}, {vb_y}, {vb_width}, {vb_height}")
            gradient_def = self.create_gradient_background(bg_color)
            icon_size = self.size - (self.padding * 2)
            icon_position = self.padding
            # Use min(vb_width, vb_height) for scale to fill the icon area
            scale_factor = icon_size / max(vb_width, vb_height)
            scaled_width = vb_width * scale_factor
            scaled_height = vb_height * scale_factor
            center_x = icon_position + (icon_size - scaled_width) / 2
            center_y = icon_position + (icon_size - scaled_height) / 2
            print(f"Scale factor: {scale_factor:.3f}")
            print(f"Positioning at: ({center_x:.1f}, {center_y:.1f})")
            app_icon_svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="{self.size}" height="{self.size}" viewBox="0 0 {self.size} {self.size}" xmlns="http://www.w3.org/2000/svg">
    {gradient_def}
    <!-- Rounded background -->
    <rect width="{self.size}" height="{self.size}" rx="{self.corner_radius}" ry="{self.corner_radius}" 
          fill="{bg_color}" />
    <!-- Original icon -->
    <g transform="translate({center_x}, {center_y}) scale({scale_factor})">
        {''.join(children_strs)}
    </g>
</svg>"""
            return app_icon_svg
        except Exception as e:
            print(f"Error processing SVG: {e}")
            return None

    def save_icon(self, svg_content: str, output_path: str, format: str = 'svg'):
        """Save the icon in the specified format"""
        if format.lower() == 'svg':
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            print(f"✅ App icon saved as: {output_path}")
        elif format.lower() == 'png':
            try:
                import cairosvg
                png_path = output_path.replace('.svg', '.png')
                cairosvg.svg2png(bytestring=svg_content.encode('utf-8'), 
                               write_to=png_path, output_width=128, output_height=128)
                print(f"✅ App icon saved as: {png_path}")
            except ImportError:
                print("⚠️  cairosvg not installed. Install with: pip install cairosvg")
                print("   Saving as SVG instead...")
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(svg_content)
                print(f"✅ App icon saved as: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python transfer_logo.py input.svg [format]")
        print("Format options: svg (default), png, both")
        sys.exit(1)
    input_path = sys.argv[1]
    format_option = sys.argv[2] if len(sys.argv) > 2 else 'svg'
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found")
        sys.exit(1)
    input_file = Path(input_path)
    output_name = f"{input_file.stem}_logo.svg"
    output_path = input_file.parent / output_name
    converter = SVGAppIconConverter()
    print(f"🔄 Processing: {input_path}")
    app_icon_svg = converter.convert_svg_to_app_icon(input_path)
    if app_icon_svg:
        if format_option.lower() in ['svg', 'both']:
            converter.save_icon(app_icon_svg, str(output_path), 'svg')
        if format_option.lower() in ['png', 'both']:
            converter.save_icon(app_icon_svg, str(output_path), 'png')
        print("🎉 Conversion complete!")
    else:
        print("❌ Conversion failed")

if __name__ == "__main__":
    main()