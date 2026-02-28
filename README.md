# Awesome 3D Gaussian Splatting

<div align="center">
  A curated collection of resources focused on 3D Gaussian Splatting (3DGS) and related technologies.

  [**Browse the Paper List**](https://mrnerf.github.io/awesome-3D-gaussian-splatting/) | [**Contribute**](CONTRIBUTING.md) | [**MrNeRF**](https://www.mrnerf.com)

</div>

## Contents

- [Papers &amp; Documentation](#papers--documentation)
- [Implementations](#implementations)
- [Viewers &amp; Game Engine Support](#viewers--game-engine-support)
- [Tools &amp; Utilities](#tools--utilities)
- [Learning Resources](#learning-resources)
- [Sponsors](#sponsors)

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

| Implementation                                                           | Language    | License    | Description                     |
| ------------------------------------------------------------------------ | ----------- | ---------- | ------------------------------- |
| [LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)                   | C++/CUDA    | GPL-3.0 | High-performance implementation |
| [Taichi 3D GS](https://github.com/wanmeihuali/taichi_3d_gaussian_splatting) | Taichi      | Apache-2.0 | Taichi-based implementation     |
| [Nerfstudio gsplat](https://github.com/nerfstudio-project/gsplat)           | Python/CUDA | Apache-2.0 | Integration with Nerfstudio     |
| [OpenSplat](https://github.com/pierotofy/OpenSplat)                         | C++/CPU/GPU | AGPL-3.0   | Cross-platform solution         |
| [Grendel](https://github.com/nyu-systems/Grendel-GS)                        | Python/CUDA | Apache-2.0 | Distributed computing focus     |
| [Warp 3DGS](https://github.com/guoriyue/3dgs-warp-scratch)                  | Warp/Python | AGPL-3.0   | Warp-based implementation       |

### Frameworks

- [Pointrix](https://github.com/pointrix-project/pointrix) - Differentiable point-based rendering
- [GauStudio](https://github.com/GAP-LAB-CUHK-SZ/gaustudio) - Unified framework with multiple implementations
- [DriveStudio](https://github.com/ziyc/drivestudio) - Urban scene reconstruction framework
- [GSCodecStudio](https://github.com/JasonLSC/GSCodec_Studio) - Compression and Dynamic splattings

## Viewers & Game Engine Support

### Game Engines

- [Unity Plugin](https://github.com/aras-p/UnityGaussianSplatting)
- [Unity Plugin (gsplat-unity)](https://github.com/wuyize25/gsplat-unity)
- [Unity Plugin (DynGsplat-unity)](https://github.com/HiFi-Human/DynGsplat-unity) - For dynamic splattings
- [Unreal Plugin (MLSLabsGaussianSplattingRenderer-UE) ](https://github.com/mlslabs/MLSLabsGaussianSplattingRenderer-UE))
- [Unreal Plugin (XV3DGS-UEPlugin)](https://github.com/xverse-engine/XV3DGS-UEPlugin)
- [PlayCanvas Engine](https://github.com/playcanvas/engine)

### Web Viewers

**WebGL**

- [Splat Viewer](https://github.com/antimatter15/splat)
- [Gauzilla](https://github.com/BladeTransformerLLC/gauzilla)
- [Interactive Viewer](https://github.com/kishimisu/Gaussian-Splatting-WebGL)
- [GaussianSplats3D](https://github.com/mkkellogg/GaussianSplats3D)
- [PlayCanvas Model Viewer](https://github.com/playcanvas/model-viewer)
- [SuperSplat Viewer](https://github.com/playcanvas/supersplat-viewer)

**WebGPU**

- [EPFL Viewer](https://github.com/cvlab-epfl/gaussian-splatting-web)
- [WebGPU Splat](https://github.com/KeKsBoTer/web-splat)

### Desktop Viewers

**Linux**

- [DearGaussianGUI](https://github.com/leviome/DearGaussianGUI)
- [LiteViz-GS](https://github.com/panxkun/liteviz-gs)

### Native Applications

- [Blender Add-on](https://github.com/ReshotAI/gaussian-splatting-blender-addon)
- [Blender Add-on (KIRI)](https://github.com/Kiri-Innovation/3dgs-render-blender-addon)
- [Blender Add-on (404—GEN)](https://github.com/404-Repo/three-gen-blender-plugin)
- [iOS Metal Viewer](https://github.com/laanlabs/metal-splats)
- [OpenGL Viewer](https://github.com/limacv/GaussianSplattingViewer)
- [VR Support (OpenXR)](https://github.com/hyperlogic/splatapult)
- [ROS2 Support](https://github.com/shadygm/ROSplat)

## Tools & Utilities

### Data Processing

- [Kapture](https://github.com/naver/kapture) - Unified data format for visual localization
- [3DGS Converter](https://github.com/francescofugazzi/3dgsconverter) - Format conversion tool
- [Point Cloud Editor](https://github.com/JohannesKrueger/pointcloudeditor) - Web-based point cloud editing
- [SPZ Converter](https://github.com/stytim/spz) - SPZ conversion tool
- [gsbox Converter](https://github.com/gotoeasy/gsbox) - PLY SPLAT SPZ SPX conversion tool
- [SplatTransform](https://github.com/playcanvas/splat-transform) - CLI tool for converting and editing splats
- [GaussForge](https://github.com/3dgscloud/GaussForge) - C++/WASM-based conversion between PLY, SPZ, SPLAT, and KSPLAT.

### Development Tools

- [GSOPs for Houdini](https://github.com/david-rhodes/GSOPs) - Houdini integration tools
- [camorph](https://github.com/Fraunhofer-IIS/camorph) - Camera parameter conversion
- [SuperSplat](https://github.com/playcanvas/supersplat) - Browser-based 3DGS editor

## Learning Resources

### Blog Posts

- [3DGS Introduction](https://huggingface.co/blog/gaussian-splatting) - HuggingFace guide
- [Implementation Details](https://github.com/kwea123/gaussian_splatting_notes) - Technical deep dive
- [Mathematical Foundation](https://github.com/chiehwangs/3d-gaussian-theory) - Theory explanation
- [Capture Guide](https://medium.com/@heyulei/capture-images-for-gaussian-splatting-81d081bbc826) - Image capture tutorial
- [PyTorch Implementation](https://myasincifci.github.io/) - Curated implementation of Vanilla 3DGS in PyTorch

### Talks

- [Gaussian Splats: Ready for Standardization?](https://www.youtube.com/watch?v=0xdPpKSkO3I) - Metaverse Standards Forum 1/28/2025
- [Unity Integration Guide](https://www.youtube.com/watch?v=pM_HV2TU4rU&t=5298s) - Metaverse Standards Forum 5/6/2025

### Video Tutorials

- [Getting Started (Windows)](https://youtu.be/UXtuigy_wYc)
- [Gaussian Splats Town Hall - Part 2](https://youtu.be/5_GaPYBHqOo)
- [Two-Minute Explanation](https://youtu.be/HVv_IQKlafQ)
- [Jupyter Tutorial](https://www.youtube.com/watch?v=OcvA7fmiZYM)

<br>

## Data
- [NERDS 360 Multi-View dataset for Outdoor Scenes](https://zubair-irshad.github.io/projects/neo360.html)

<br>

## Courses
- [MIT Inverse Rendering Lectures (Module 2)](https://www.scenerepresentations.org/courses/inverse-graphics-23/)

<br>

## Open Source Implementations 
### Reference 
- [Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting)

### Unofficial Implementations
|                                                                                             | Language       | License    |
|---------------------------------------------------------------------------------------------|----------------|------------|
| [Taichi 3D Gaussian Splatting](https://github.com/wanmeihuali/taichi_3d_gaussian_splatting) | taichi         | Apache-2.0 |
| [Gaussian Splatting 3D](https://github.com/heheyas/gaussian_splatting_3d)                   | Python/CUDA    |            |
| [3D Gaussian Splatting](https://github.com/WangFeng18/3d-gaussian-splatting)                | Python/CUDA    | MIT        |
| [fast](https://github.com/MrNeRF/gaussian-splatting-cuda)                                   | C++/CUDA       | Inria/MPII |
| [nerfstudio](https://github.com/nerfstudio-project/gsplat)                                  | Python/CUDA    | Apache-2.0 |
| [taichi-splatting](https://github.com/uc-vision/taichi-splatting)                           | taichi/PyTorch | Apache-2.0 |
| [OpenSplat](https://github.com/pierotofy/OpenSplat)                                         | C++/CPU or GPU | AGPL-3.0   |
| [3D Gaussian Splatting](https://github.com/joeyan/gaussian_splatting)                       | Python/CUDA    | MIT        |
| [Grendel Distributed 3DGS](https://github.com/nyu-systems/Grendel-GS)                       | Python/CUDA    | Apache-2.0 |

### 2D Gaussian Splatting
- [jupyter notebook 2D GS splatting](https://github.com/OutofAi/2D-Gaussian-Splatting)

### Gaussian Style Transfer 
- [Direct Gaussian Style Optimization (DGSO): Stylizing 3D Gaussian Splats](https://github.com/An-u-rag/stylized-gaussian-splatting) - Applying style transfer during gaussian optimization to produce stylized gaussian splats of a scene.

### Game Engines 
- [Unity](https://github.com/aras-p/UnityGaussianSplatting)
- [PlayCanvas](https://github.com/playcanvas/engine/tree/main/src/scene/gsplat)
- [Unreal](https://github.com/xverse-engine/XV3DGS-UEPlugin)

### Viewers
- [WebGL Viewer 1](https://github.com/antimatter15/splat)
- [WebGL Viewer 2](https://github.com/kishimisu/Gaussian-Splatting-WebGL)
- [WebGL Viewer 3](https://github.com/BladeTransformerLLC/gauzilla)
- [WebGPU Viewer 1](https://github.com/cvlab-epfl/gaussian-splatting-web)
- [WebGPU Viewer 2](https://github.com/MarcusAndreasSvensson/gaussian-splatting-webgpu)
- [WebGPU Viewer 3](https://github.com/KeKsBoTer/web-splat)
- [Three.js](https://github.com/mkkellogg/GaussianSplats3D)
- [A-Frame](https://github.com/quadjr/aframe-gaussian-splatting)
- [Nerfstudio Unofficial](https://github.com/yzslab/nerfstudio/tree/gaussian_splatting)
- [Nerfstudio Viser](https://github.com/nerfstudio-project/viser)
- [Blender (Editor)](https://github.com/ReshotAI/gaussian-splatting-blender-addon/tree/master)
- [WebRTC viewer](https://github.com/dylanebert/gaussian-viewer)
- [iOS & Metal viewer](https://github.com/laanlabs/metal-splats)
- [jupyter notebook](https://github.com/shumash/gaussian-splatting/blob/mshugrina/interactive/interactive.ipynb)
- [PyOpenGL viewer (also with official CUDA backend)](https://github.com/limacv/GaussianSplattingViewer.git)
- [PlayCanvas Viewer](https://github.com/playcanvas/model-viewer)
- [gsplat.js](https://github.com/dylanebert/gsplat.js)
- [Splatapult](https://github.com/hyperlogic/splatapult) - 3d gaussian splatting renderer in C++ and OpenGL, works with OpenXR for tethered VR
- [3DGS.cpp](https://github.com/shg8/3DGS.cpp) - cross-platform, high performance 3DGS renderer in C++ and Vulkan Compute, supporting Windows, macOS, Linux, iOS, and visionOS
- [vkgs](https://github.com/jaesung-cs/vkgs) - cross-platform, high performance 3DGS renderer in C++ and Vulkan Compute/Graphics
- [spaTV](https://github.com/antimatter15/splaTV) - WebGL Viewer for 4D Gaussians (based on SpaceTime Gaussian) with demo [here](http://antimatter15.com/splaTV/)
- [Taichi Viewer](https://github.com/uc-vision/splat-viewer)
- [uc-vision-splat-viewer](https://github.com/uc-vision/splat-viewer)(3D gaussin splatting renderer with benchmarking capability)
- [splatviz](https://github.com/Florian-Barthel/splatviz) - Viewer that allows you to edit the rendering code during runtime or to display multiple scenes at once.
- [Houdini Gaussian Splatting Viewport Renderer](https://github.com/rubendhz/houdini-gsplat-renderer) - A HDK/GLSL implementation of Gaussian Splatting in Houdini

### Utilities
- [Kapture](https://github.com/naver/kapture) - A unified data format to facilitate visual localization and structure from motion e.g. for bundler to colmap model conversion
- [Kapture image cropper script](https://gist.github.com/jo-chemla/258e6e40d3d6c2220b29518ff3c17c40) - Undistorted image cropper script to remove black borders with included conversion instructions
- [camorph](https://github.com/Fraunhofer-IIS/camorph) - A toolbox for conversion between camera parameter conventions e.g. Reality Capture to colmap model
- [3DGS Converter](https://github.com/francescofugazzi/3dgsconverter) - A tool for converting 3D Gaussian Splatting .ply files into a format suitable for Cloud Compare and vice-versa
- [SuperSplat](https://github.com/playcanvas/super-splat) - Open source browser-based tool to clean/filter, reorient and compress .ply/.splat files
- [SpectacularAI](https://github.com/SpectacularAI/point-cloud-tools) - Conversion scripts for different 3DGS conventions
- [GSOPs](https://github.com/david-rhodes/GSOPs) - GSOPs (Gaussian Splat Operators) for SideFX Houdini. Import, edit, and export models, or generate synthetic training data
- [Point Cloud Editor](https://github.com/JohannesKrueger/pointcloudeditor) - Clean and edit pointclouds from that are in colmap sparse format in a browser to improve reconstruction results

### Tutorial
- [Tutorial from the authors of 3DGS](https://3dgstutorial.github.io/)

### Framework
- [Pointrix](https://github.com/pointrix-project/pointrix) - A differentiable point-based rendering framework.
- [msplat](https://github.com/pointrix-project/msplat) - A modular differential gaussian rasterization library.
- [GauStudio](https://github.com/GAP-LAB-CUHK-SZ/gaustudio) - Unified framework with different paper implementations
- [DriveStudio](https://github.com/ziyc/drivestudio) - A 3DGS framework for omni urban scene reconstruction and simulation.
- [gaussian-splatting-lightning](https://github.com/yzslab/gaussian-splatting-lightning) - A 3D Gaussian Splatting framework with various derived algorithms and an interactive web viewer

### Other
- [My-exp-Gaussians](https://github.com/ingra14m/My-exp-Gaussians) - Enhancing the ability of 3D Gaussians to model complex scenes
- [360-gaussian-splatting](https://github.com/inuex35/360-gaussian-splatting) - Generate gaussian splatting directly from 360 images


## Blog Posts

1. [Gaussian Splatting is pretty cool](https://aras-p.info/blog/2023/09/05/Gaussian-Splatting-is-pretty-cool/)
2. [Making Gaussian Splats smaller](https://aras-p.info/blog/2023/09/13/Making-Gaussian-Splats-smaller/)
3. [Making Gaussian Splats more smaller](https://aras-p.info/blog/2023/09/27/Making-Gaussian-Splats-more-smaller/)
4. [Introduction to 3D Gaussian Splatting](https://huggingface.co/blog/gaussian-splatting)
5. [Very good (technical) intro to 3D Gaussian Splatting](https://medium.com/@AriaLeeNotAriel/numbynum-3d-gaussian-splatting-for-real-time-radiance-field-rendering-kerbl-et-al-60c0b25e5544)
6. [Write up on some mathematical details of the 3DGS implementation](https://github.com/kwea123/gaussian_splatting_notes)
7. [Discussion about gs universal format](https://github.com/mkkellogg/GaussianSplats3D/issues/47#issuecomment-1801360116)
8. [Math explanation to understand 3DGS](https://github.com/chiehwangs/3d-gaussian-theory)
9. [Compressing Gaussian Splats](https://blog.playcanvas.com/compressing-gaussian-splats/)
10. [Comprehensive overview of Gaussian Splatting](https://towardsdatascience.com/a-comprehensive-overview-of-gaussian-splatting-e7d570081362)
11. [Gaussian Head Avatars: A Summary](https://towardsdatascience.com/gaussian-head-avatars-a-summary-2bd17bd48500)
12. [NeRFs vs. 3DGS](https://edwardahn.me/writing/NeRFvs3DGS/)
13. [Howto capture images for 3DGS](https://medium.com/@heyulei/capture-images-for-gaussian-splatting-81d081bbc826)
14. [Mathematical details of forward and backward passes](https://github.com/joeyan/gaussian_splatting/blob/main/MATH.md)
15. [3D in Geospatial: NeRFs, Gaussian Splatting, and Spatial Computing](https://ckoziol.com/blog/2024/radiance_methods/)

## Tutorial Videos

1. [Getting Started with 3DGS for Windows](https://youtu.be/UXtuigy_wYc?si=j1vfORNspcocSH-b)
2. [How to view 3DGS Scenes in Unity](https://youtu.be/5_GaPYBHqOo?si=6u9j1HqXwF_5WSUL)
3. [Two-minute explanation of 3DGS](https://youtu.be/HVv_IQKlafQ?si=w5c9XKHfKIBuXDLW)
4. [Jupyter notebook tutorial](https://www.youtube.com/watch?v=OcvA7fmiZYM&t=2s)
5. [Intro to gaussian splatting (and Unity plugin)](https://www.xuanprada.com/blog/2023/10/22/intro-to-gaussian-splatting)
6. [Computerphile 3DGS explanation](https://youtu.be/VkIJbpdTujE?si=1GLjzBfF9LCuT22o)

## Credits

- Thanks to [Leonid Keselman](https://github.com/leonidk) for informing me about the release of the paper "Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting".
- Thanks to [Eric Haines](https://github.com/erich666) for suggesting the jupyter notebook viewer, windows tutorial and for fixing text hyphenations and other issues.
- Thanks to [Henry Pearce](https://github.com/henrypearce4D) for maintaining contributions.
=======
- [Yehe Liu](https://x.com/YeheLiu)
>>>>>>> 7656f5e7ed3bc239fae0e9a8e1990be82bd7daa9
