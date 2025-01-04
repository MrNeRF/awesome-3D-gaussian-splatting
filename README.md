# Awesome 3D Gaussian Splatting

<div align="center">
  A curated collection of resources focused on 3D Gaussian Splatting (3DGS) and related technologies.
  
  [**Browse the Paper List**](https://mrnerf.github.io/awesome-3D-gaussian-splatting/) | [**Contribute**](CONTRIBUTING.md)
</div>

## Contents

- [Papers & Documentation](#papers--documentation)
- [Implementations](#implementations)
- [Viewers & Game Engine Support](#viewers--game-engine-support)
- [Tools & Utilities](#tools--utilities)
- [Learning Resources](#learning-resources)

## Papers & Documentation

### Papers Database
Visit our comprehensive, searchable database of 3D Gaussian Splatting papers:  
[Papers Database](https://mrnerf.github.io/awesome-3D-gaussian-splatting/)

### Courses
- [MIT Inverse Rendering Lectures (Module 2)](https://www.scenerepresentations.org/courses/inverse-graphics-23/) - Academic deep dive into inverse rendering

### Datasets
- [NERDS 360 Multi-View dataset](https://zubair-irshad.github.io/projects/neo360.html) - High-quality outdoor scene dataset

## Implementations

### Official Reference
- [Original Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) - The reference implementation by the original authors

### Community Implementations
| Implementation | Language | License | Description |
|----------------|----------|----------|-------------|
| [Taichi 3D GS](https://github.com/wanmeihuali/taichi_3d_gaussian_splatting) | Taichi | Apache-2.0 | Taichi-based implementation |
| [Nerfstudio gsplat](https://github.com/nerfstudio-project/gsplat) | Python/CUDA | Apache-2.0 | Integration with Nerfstudio |
| [fast](https://github.com/MrNeRF/gaussian-splatting-cuda) | C++/CUDA | Inria/MPII | High-performance implementation |
| [OpenSplat](https://github.com/pierotofy/OpenSplat) | C++/CPU/GPU | AGPL-3.0 | Cross-platform solution |
| [Grendel](https://github.com/nyu-systems/Grendel-GS) | Python/CUDA | Apache-2.0 | Distributed computing focus |

### Frameworks
- [Pointrix](https://github.com/pointrix-project/pointrix) - Differentiable point-based rendering
- [GauStudio](https://github.com/GAP-LAB-CUHK-SZ/gaustudio) - Unified framework with multiple implementations
- [DriveStudio](https://github.com/ziyc/drivestudio) - Urban scene reconstruction framework

## Viewers & Game Engine Support

### Game Engines
- [Unity Plugin](https://github.com/aras-p/UnityGaussianSplatting)
- [Unreal Plugin](https://github.com/xverse-engine/XV3DGS-UEPlugin)
- [PlayCanvas Integration](https://github.com/playcanvas/engine/tree/main/src/scene/gsplat)

### Web Viewers
**WebGL**
- [Splat Viewer](https://github.com/antimatter15/splat)
- [Gauzilla](https://github.com/BladeTransformerLLC/gauzilla)
- [Interactive Viewer](https://github.com/kishimisu/Gaussian-Splatting-WebGL)

**WebGPU**
- [EPFL Viewer](https://github.com/cvlab-epfl/gaussian-splatting-web)
- [WebGPU Splat](https://github.com/KeKsBoTer/web-splat)

### Native Applications
- [Blender Add-on](https://github.com/ReshotAI/gaussian-splatting-blender-addon)
- [iOS Metal Viewer](https://github.com/laanlabs/metal-splats)
- [OpenGL Viewer](https://github.com/limacv/GaussianSplattingViewer)
- [VR Support (OpenXR)](https://github.com/hyperlogic/splatapult)

## Tools & Utilities

### Data Processing
- [Kapture](https://github.com/naver/kapture) - Unified data format for visual localization
- [3DGS Converter](https://github.com/francescofugazzi/3dgsconverter) - Format conversion tool
- [SuperSplat](https://github.com/playcanvas/super-splat) - Browser-based cleanup tool
- [Point Cloud Editor](https://github.com/JohannesKrueger/pointcloudeditor) - Web-based point cloud editing

### Development Tools
- [GSOPs for Houdini](https://github.com/david-rhodes/GSOPs) - Houdini integration tools
- [camorph](https://github.com/Fraunhofer-IIS/camorph) - Camera parameter conversion

## Learning Resources

### Blog Posts
- [3DGS Introduction](https://huggingface.co/blog/gaussian-splatting) - HuggingFace guide
- [Implementation Details](https://github.com/kwea123/gaussian_splatting_notes) - Technical deep dive
- [Mathematical Foundation](https://github.com/chiehwangs/3d-gaussian-theory) - Theory explanation
- [Capture Guide](https://medium.com/@heyulei/capture-images-for-gaussian-splatting-81d081bbc826) - Image capture tutorial

### Video Tutorials
- [Getting Started (Windows)](https://youtu.be/UXtuigy_wYc)
- [Unity Integration Guide](https://youtu.be/5_GaPYBHqOo)
- [Two-Minute Explanation](https://youtu.be/HVv_IQKlafQ)
- [Jupyter Tutorial](https://www.youtube.com/watch?v=OcvA7fmiZYM)
