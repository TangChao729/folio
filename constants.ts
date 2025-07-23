// Copyright Taylor Tang 2025. All Rights Reserved.
// Project: portfolio
// Author contact: https://www.linkedin.com/in/taylor-tang/
// This file is licensed under the MIT License.
// License text available at https://opensource.org/licenses/MIT

export const METADATA = {
  title: "Portfolio | Taylor Tang",
  description:
    "ML Engineer building AI systems that bridge cutting-edge research with real-world impact",
  siteUrl: "https://taylortang.dev/", // Update with your actual domain
};

export const MENULINKS = [
  {
    name: "Home",
    ref: "home",
  },
  {
    name: "Works",
    ref: "works",
  },
  {
    name: "Skills",
    ref: "skills",
  },
  {
    name: "Timeline",
    ref: "timeline",
  },
  {
    name: "Contact",
    ref: "contact",
  },
];

export const TYPED_STRINGS = [
  "I build AI systems that solve real problems",
  "I develop computer vision solutions",
  "I create intelligent automation pipelines",
  "I bridge research with production ML",
];

export const EMAIL = "tay.tang@outlook.com";

export const SOCIAL_LINKS = {
  linkedin: "https://www.linkedin.com/in/taylor-tang/",
  github: "https://github.com/TangChao729",
};

export interface IProject {
  name: string;
  image: string;
  blurImage: string;
  description: string;
  gradient: [string, string];
  url: string;
  tech: string[];
}

export const PROJECTS: IProject[] = [
  {
    name: "AI Agents Red Team Testing",
    image: "/projects/red-teaming-test.png",
    blurImage: "/projects/blur/red-teaming-test-blur.png",
    description: "Led red team testing of commercial AI agentic framework, executing 5,000+ test cases across 15 attack vectors.",
    gradient: ["#FF6B6B", "#EE5A24"],
    url: "#",
    tech: ["python", "promptfoo", "claude", "openai"],
  },
  {
    name: "Australia Age Assurance Technology Trial",
    image: "/projects/aatt.png",
    blurImage: "/projects/blur/aatt-blur.png",
    description: "Built testing platform for Australia Age Assurance Trial, facilitating testing with 1,100+ participants.",
    gradient: ["#0052D4", "#4364F7"],
    url: "#",
    tech: ["react", "typescript", "face-rec", "postgresql", "aws"],
  },
  {
    name: "Feral Animal Detection System",
    image: "/projects/feral-ai.png",
    blurImage: "/projects/blur/feral-ai-blur.png",
    description: "Detected feral animals using thermal drone footage to support wildlife management.",
    gradient: ["#667eea", "#764ba2"],
    url: "#",
    tech: ["pytorch", "yolo", "cvat", "drone", "clearml"],
  },
  {
    name: "AI-Powered Game Industry Intelligence",
    image: "/projects/game_pulse.png",
    blurImage: "/projects/blur/game_pulse-blur.png",
    description: "Automated intelligence system processing steam & reddit data, reducing manual research time by 80%.",
    gradient: ["#00C9FF", "#92FE9D"],
    url: "#",
    tech: ["react", "python", "openai", "claude", "vectordb"],
  },
  {
    name: "Road Safety Monitoring System",
    image: "/projects/roadscan.png",
    blurImage: "/projects/blur/roadscan-blur.png",
    description: "Urban management assistant analyzing road footage for potholes & cracks for quicker, targeted repairs.",
    gradient: ["#FC466B", "#3F5EFB"],
    url: "#",
    tech: ["pytorch", "yolo", "gcp"],
  },
  {
    name: "National Bushfire Analysis Using Satellite Imagery",
    image: "/projects/bushfire.png",
    blurImage: "/projects/blur/bushfire-blur.png",
    description: "Published paper at IEEE eScience 2024, using satellite imagery & computer vision to detect bushfires.",
    gradient: ["#fa709a", "#fee140"],
    url: "#",
    tech: ["pytorch", "nvidia", "satellite", "gcp"],
  },
];

export const SKILLS = {
  "Programming": [
    "python",
    "javascript",
    "typescript",
    "git",
  ],
  "Computer Vision": [
    "pytorch",
    "yolo",
    "huggingface",
  ],
  "Large Language Models": [
    "ollama",
    "claude",
    "clip",
  ],
  "Cloud Computing": [
    "aws",
    "gcp",
    "azure",
  ]
};

export enum Branch {
  LEFT = "leftSide",
  RIGHT = "rightSide",
}

export enum NodeTypes {
  CONVERGE = "converge",
  DIVERGE = "diverge",
  CHECKPOINT = "checkpoint",
}

export enum ItemSize {
  SMALL = "small",
  LARGE = "large",
}

export const TIMELINE: Array<TimelineNodeV2> = [

  {
    type: NodeTypes.CHECKPOINT,
    title: "2024",
    size: ItemSize.LARGE,
    shouldDrawLine: false,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "Joined KJR",
    size: ItemSize.SMALL,
    subtitle:
      "As a Machine Learning Consultant",
    image: "/timeline/9_kjr.png",
    slideImage: "/timeline/9_join_kjr.PNG",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "Awards & Achievements",
    size: ItemSize.SMALL,
    subtitle:
      "My hall of fame",
    image: "/timeline/4_uom.jpg",
    slideImage: "/timeline/6_hall_of_fame.jpg",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "Published first research paper ",
    size: ItemSize.SMALL,
    subtitle:
      "At IEEE eScience 2024",
    image: "/timeline/4_uom.jpg",
    slideImage: "/timeline/7_eScience.jpeg",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "Graduated with Distinction",
    size: ItemSize.SMALL,
    subtitle:
      "From The University of Melbourne",
    image: "/timeline/4_uom.jpg",
    slideImage: "/timeline/6_graduation.jpg",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "Started internship at Vision HQ",
    size: ItemSize.SMALL,
    subtitle:
      "Developed computer vision system for road safety monitoring",
    image: "/timeline/8_vision_hq.jpeg",
    slideImage: "/timeline/8_road_scan.png",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "2023",
    size: ItemSize.LARGE,
    shouldDrawLine: false,
    alignment: Branch.LEFT,
  },

  {
    type: NodeTypes.CHECKPOINT,
    title: "Dean's Award",
    size: ItemSize.SMALL,
    subtitle:
      "Recipient of the Dean's Award for academic excellence",
    image: "/timeline/4_uom.jpg",
    slideImage: "/timeline/5_dean.JPG",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "Master of IT (AI Major)",
    size: ItemSize.SMALL,
    subtitle:
      "Enrolled at The University of Melbourne",
    image: "/timeline/4_uom.jpg",
    slideImage: "/timeline/4_uom_welcome.jpg",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "2022",
    size: ItemSize.LARGE,
    shouldDrawLine: false,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "Learning to code",
    size: ItemSize.SMALL,
    subtitle:
      "Self-supervised coding study on Coursera.",
    image: "/timeline/3_coursera.png",
    slideImage: "/timeline/3_pong2.png",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "2021",
    size: ItemSize.LARGE,
    shouldDrawLine: false,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "Quit Project Manager job",
    size: ItemSize.SMALL,
    subtitle:
      "To pursue my passion for programming",
    image: "/timeline/2_tnt.png",
    slideImage: "/timeline/2_pm.JPG",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "2016",
    size: ItemSize.LARGE,
    shouldDrawLine: false,
    alignment: Branch.LEFT,
  },
  {
    type: NodeTypes.CHECKPOINT,
    title: "Dive Instructor",
    size: ItemSize.SMALL,
    subtitle:
      "Worked as a dive instructor at Tangalooma Island Resort",
    image: "/timeline/1_tangalooma.webp",
    slideImage: "/timeline/1_dive_instructor.jpg",
    shouldDrawLine: true,
    alignment: Branch.LEFT,
  },
];

export type TimelineNodeV2 = CheckpointNode | BranchNode;

export interface CheckpointNode {
  type: NodeTypes.CHECKPOINT;
  title: string;
  subtitle?: string;
  size: ItemSize;
  image?: string;
  slideImage?: string;
  shouldDrawLine: boolean;
  alignment: Branch;
}

export interface BranchNode {
  type: NodeTypes.CONVERGE | NodeTypes.DIVERGE;
}

export const GTAG = "UA-163844688-1"; // Update with your Google Analytics ID if you want tracking