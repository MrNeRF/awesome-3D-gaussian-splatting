# Awesome 3D Gaussian Splatting

<div align="center">
  A curated collection of resources focused on 3D Gaussian Splatting (3DGS) and related technologies.

  [**Browse the Paper List**](https://mrnerf.github.io/awesome-3D-gaussian-splatting/) | [**LichtFeld Studio**](https://lichtfeld.io) | [**Contribute**](CONTRIBUTING.md) | [**MrNeRF**](https://www.mrnerf.com)

</div>

## Contents

- [Papers &amp; Documentation](#papers--documentation)
- [Implementations](#implementations)
- [Viewers &amp; Game Engine Support](#viewers--game-engine-support)
- [Tools &amp; Utilities](#tools--utilities)
- [Learning Resources](#learning-resources)
- [Credits](#credits)

## Papers & Documentation

### Papers Database

Visit our comprehensive, searchable database of 3D Gaussian Splatting papers:
[Papers Database](https://mrnerf.github.io/awesome-3D-gaussian-splatting/)

### Courses & Tutorials

- [MIT Inverse Rendering Lectures (Module 2)](https://www.scenerepresentations.org/courses/inverse-graphics-23/) - Academic deep dive into inverse rendering
- [3DGS Tutorial](https://3dgstutorial.github.io/) - Tutorial from the authors of the original 3DGS paper

### Datasets

- [NERDS 360 Multi-View dataset](https://zubair-irshad.github.io/projects/neo360.html) - High-quality outdoor scene dataset

## Implementations

### Official Reference

- [Original Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) - The reference implementation by the original authors

### Community Implementations

| Implementation | Language | License | Description |
| -------------- | -------- | ------- | ----------- |
| [LichtFeld Studio](https://github.com/MrNeRF/LichtFeld-Studio) ([lichtfeld.io](https://lichtfeld.io)) | C++/CUDA | GPL-3.0 | The modular workstation for 3D Gaussian Splatting — train, inspect, edit, automate, and export from a single native app |
| [Nerfstudio gsplat](https://github.com/nerfstudio-project/gsplat) | Python/CUDA | Apache-2.0 | Integration with Nerfstudio |
| [OpenSplat](https://github.com/pierotofy/OpenSplat) | C++/CPU/GPU | AGPL-3.0 | Cross-platform solution |
| [Taichi 3D GS](https://github.com/wanmeihuali/taichi_3d_gaussian_splatting) | Taichi | Apache-2.0 | Taichi-based implementation |
| [taichi-splatting](https://github.com/uc-vision/taichi-splatting) | Taichi/PyTorch | Apache-2.0 | Modular rasterizer for Taichi and PyTorch |
| [Grendel Distributed 3DGS](https://github.com/nyu-systems/Grendel-GS) | Python/CUDA | Apache-2.0 | Multi-GPU distributed training |
| [Warp 3DGS](https://github.com/guoriyue/3dgs-warp-scratch) | Warp/Python | AGPL-3.0 | Warp-based implementation |
| [RI3D](https://github.com/Asus-Monitor/ri3d-impl) | Python/CUDA | Unlicense | Few-shot gaussian splatting pipeline |
| [gaussian_splatting](https://github.com/joeyan/gaussian_splatting) | Python/CUDA | MIT | Readable implementation with a [written derivation of the math](https://github.com/joeyan/gaussian_splatting/blob/main/MATH.md) |
| [3d-gaussian-splatting](https://github.com/WangFeng18/3d-gaussian-splatting) | Python/CUDA | MIT | Compact reimplementation |
| [gaussian_splatting_3d](https://github.com/heheyas/gaussian_splatting_3d) | Python/CUDA | | Early community reimplementation |
| [My-exp-Gaussians](https://github.com/ingra14m/My-exp-Gaussian) | Python/CUDA | | Enhances the ability of 3D Gaussians to model complex scenes |
| [360-gaussian-splatting](https://github.com/inuex35/360-gaussian-splatting) | Python | | Trains splats directly from 360° images |
| [2D Gaussian Splatting](https://github.com/OutofAi/2D-Gaussian-Splatting) | Jupyter | MIT | Notebook walkthrough of 2D gaussian splatting |
| [DGSO](https://github.com/An-u-rag/stylized-gaussian-splatting) | Python | MIT | Style transfer applied during gaussian optimization |

### Frameworks

- [Pointrix](https://github.com/pointrix-project/pointrix) - Differentiable point-based rendering
- [msplat](https://github.com/pointrix-project/msplat) - Modular differential gaussian rasterization library
- [GauStudio](https://github.com/GAP-LAB-CUHK-SZ/gaustudio) - Unified framework with multiple implementations
- [DriveStudio](https://github.com/ziyc/drivestudio) - Urban scene reconstruction framework
- [GSCodecStudio](https://github.com/JasonLSC/GSCodec_Studio) - Compression and Dynamic splattings
- [gaussian-splatting-lightning](https://github.com/yzslab/gaussian-splatting-lightning) - Derived algorithms plus an interactive web viewer

## Viewers & Game Engine Support

### Game Engines

- [Unity Plugin](https://github.com/aras-p/UnityGaussianSplatting)
- [Unity Plugin (gsplat-unity)](https://github.com/wuyize25/gsplat-unity)
- [Unity Plugin (DynGsplat-unity)](https://github.com/HiFi-Human/DynGsplat-unity) - For dynamic splattings
- [Unreal Plugin (MLSLabsGaussianSplattingRenderer-UE)](https://github.com/mlslabs/MLSLabsGaussianSplattingRenderer-UE)
- [Unreal Plugin (XScene-UEPlugin)](https://github.com/xverse-engine/XScene-UEPlugin)
- [PlayCanvas Engine](https://github.com/playcanvas/engine)
- [Godot Plugin (gdgs)](https://github.com/ReconWorldLab/godot-gaussian-splatting) - Real-time 3DGS rendering plugin for Godot 4.3+

### Web Viewers

**WebGL**

- [Splat Viewer](https://github.com/antimatter15/splat)
- [Gauzilla](https://github.com/BladeTransformerLLC/gauzilla)
- [Interactive Viewer](https://github.com/kishimisu/Gaussian-Splatting-WebGL)
- [GaussianSplats3D](https://github.com/mkkellogg/GaussianSplats3D)
- [gsplat.js](https://github.com/huggingface/gsplat.js)
- [A-Frame](https://github.com/quadjr/aframe-gaussian-splatting)
- [splaTV](https://github.com/antimatter15/splaTV) - Viewer for 4D Gaussians, with a [live demo](http://antimatter15.com/splaTV/)
- [WebRTC viewer](https://github.com/dylanebert/gaussian-viewer)

**WebGPU**

- [EPFL Viewer](https://github.com/cvlab-epfl/gaussian-splatting-web)
- [WebGPU Splat](https://github.com/KeKsBoTer/web-splat)
- [gaussian-splatting-webgpu](https://github.com/MarcusAndreasSvensson/gaussian-splatting-webgpu)
- [SuperSplat Viewer](https://github.com/playcanvas/supersplat-viewer) - High-performance splat viewer
- [PlayCanvas Model Viewer](https://github.com/playcanvas/model-viewer) - Viewer for glTF and 3DGS assets

### Desktop Viewers

- [3DGS.cpp](https://github.com/shg8/3DGS.cpp) - C++/Vulkan renderer for Windows, macOS, Linux, iOS and visionOS
- [vkgs](https://github.com/jaesung-cs/vkgs) - Cross-platform C++/Vulkan renderer
- [splatviz](https://github.com/Florian-Barthel/splatviz) - Edit the rendering code at runtime or display multiple scenes at once
- [OpenGL Viewer](https://github.com/limacv/GaussianSplattingViewer) - PyOpenGL viewer, also with official CUDA backend
- [Taichi Viewer](https://github.com/uc-vision/splat-viewer) - Renderer with benchmarking capability
- [DearGaussianGUI](https://github.com/leviome/DearGaussianGUI)
- [LiteViz-GS](https://github.com/panxkun/liteviz-gs)
- [Nerfstudio Viser](https://github.com/viser-project/viser)
- [Nerfstudio (gaussian_splatting branch)](https://github.com/yzslab/nerfstudio/tree/gaussian_splatting)
- [Jupyter notebook viewer](https://github.com/shumash/gaussian-splatting/blob/mshugrina/interactive/interactive.ipynb)

### Native Applications

- [Blender Add-on](https://github.com/ReshotAI/gaussian-splatting-blender-addon)
- [Blender Add-on (KIRI)](https://github.com/Kiri-Innovation/3dgs-render-blender-addon)
- [Blender Add-on (404—GEN)](https://github.com/404-Repo/404-gen-blender-add-on)
- [Houdini Viewport Renderer](https://github.com/rubendhz/houdini-gsplat-renderer) - HDK/GLSL implementation of Gaussian Splatting in Houdini
- [iOS Metal Viewer](https://github.com/laanlabs/metal-splats)
- [VR Support (OpenXR)](https://github.com/hyperlogic/splatapult)
- [ROS2 Support](https://github.com/shadygm/ROSplat)
- [Splat Local](https://github.com/michael-L-i/splat-local) - Video-to-3DGS pipeline running fully locally on Apple Silicon (COLMAP/GLOMAP poses, Metal-native training via Brush), with training checkpoints streamed live into a browser viewer

## Tools & Utilities

### Data Processing

- [Kapture](https://github.com/naver/kapture) - Unified data format for visual localization
- [Kapture image cropper](https://gist.github.com/jo-chemla/258e6e40d3d6c2220b29518ff3c17c40) - Undistorted image cropper to remove black borders
- [3DGS Converter](https://github.com/francescofugazzi/3dgsconverter) - Format conversion tool
- [Point Cloud Editor](https://github.com/JohannesKrueger/pointcloudeditor) - Web-based point cloud editing
- [SPZ Converter](https://github.com/stytim/spz) - SPZ conversion tool
- [gsbox Converter](https://github.com/gotoeasy/gsbox) - PLY SPLAT SPZ SPX conversion tool
- [SplatTransform](https://github.com/playcanvas/splat-transform) - CLI tool and Node/browser library for converting and editing splats, reads PLY, SOG, SPZ, SPLAT, KSPLAT and LCC/LCC2, writes PLY, SOG, SPZ, GLB, CSV, LOD and WebP
- [GaussForge](https://github.com/3dgscloud/GaussForge) - C++/WASM-based conversion between PLY, SPZ, SPLAT, and KSPLAT
- [SpectacularAI](https://github.com/SpectacularAI/point-cloud-tools) - Conversion scripts for different 3DGS conventions
- [VGGT Factor Refinement](https://github.com/jashshah999/vggt-factor-refinement) - COLMAP-free pipeline using VGGT + factor graph, from video to COLMAP-format output
- [splatreg](https://github.com/Archerkattri/splatreg) - pip-installable splat registration: align & merge two 3DGS scans into one SE(3)/Sim(3) frame (recovers scale), CLI + pure-PyTorch API, no manual gizmo
- [AURA](https://github.com/Archerkattri/aura) - Calibrated per-splat confidence for 3DGS assets: held-out reliability labels, isotonic calibration, and a distribution-free conformal pruning certificate with a certified LOD ladder; exports via glTF/OpenUSD/SPZ (pip install aura-splat)

### Development Tools

- [GSOPs for Houdini](https://github.com/cgnomads/GSOPs) - Houdini integration tools
- [camorph](https://github.com/Fraunhofer-IIS/camorph) - Camera parameter conversion
- [SuperSplat](https://github.com/playcanvas/supersplat) - Free, open source browser-based 3DGS editor with one-click publishing

## Learning Resources

### Blog Posts

- [3DGS Introduction](https://huggingface.co/blog/gaussian-splatting) - HuggingFace guide
- [Comprehensive overview of Gaussian Splatting](https://towardsdatascience.com/a-comprehensive-overview-of-gaussian-splatting-e7d570081362)
- [Very good (technical) intro to 3D Gaussian Splatting](https://medium.com/@AriaLeeNotAriel/numbynum-3d-gaussian-splatting-for-real-time-radiance-field-rendering-kerbl-et-al-60c0b25e5544)
- [Gaussian Splatting is pretty cool](https://aras-p.info/blog/2023/09/05/Gaussian-Splatting-is-pretty-cool/)
- [Making Gaussian Splats smaller](https://aras-p.info/blog/2023/09/13/Making-Gaussian-Splats-smaller/)
- [Making Gaussian Splats more smaller](https://aras-p.info/blog/2023/09/27/Making-Gaussian-Splats-more-smaller/)
- [Compressing Gaussian Splats](https://blog.playcanvas.com/compressing-gaussian-splats/)
- [PlayCanvas Open Sources SOG](https://blog.playcanvas.com/playcanvas-open-sources-sog-format-for-gaussian-splatting/) - Spatially Ordered Gaussians, a super-compressed format based on WebP that is 15-20x smaller than PLY
- [Implementation Details](https://github.com/kwea123/gaussian_splatting_notes) - Technical deep dive
- [Mathematical Foundation](https://github.com/chiehwangs/3d-gaussian-theory) - Theory explanation
- [Mathematical details of forward and backward passes](https://github.com/joeyan/gaussian_splatting/blob/main/MATH.md)
- [PyTorch Implementation](https://myasincifci.github.io/) - Curated implementation of Vanilla 3DGS in PyTorch
- [NeRFs vs. 3DGS](https://edwardahn.me/writing/NeRFvs3DGS/)
- [Gaussian Head Avatars: A Summary](https://towardsdatascience.com/gaussian-head-avatars-a-summary-2bd17bd48500)
- [3D in Geospatial: NeRFs, Gaussian Splatting, and Spatial Computing](https://ckoziol.com/blog/2024/radiance_methods/)
- [Capture Guide](https://medium.com/@heyulei/capture-images-for-gaussian-splatting-81d081bbc826) - Image capture tutorial
- [Discussion about gs universal format](https://github.com/mkkellogg/GaussianSplats3D/issues/47#issuecomment-1801360116)

### Talks

- [Gaussian Splats: Ready for Standardization?](https://www.youtube.com/watch?v=0xdPpKSkO3I) - Metaverse Standards Forum 1/28/2025
- [Unity Integration Guide](https://www.youtube.com/watch?v=pM_HV2TU4rU&t=5298s) - Metaverse Standards Forum 5/6/2025

### Video Tutorials

- [Getting Started (Windows)](https://youtu.be/UXtuigy_wYc)
- [Two-Minute Explanation](https://youtu.be/HVv_IQKlafQ)
- [Computerphile 3DGS explanation](https://youtu.be/VkIJbpdTujE)
- [Gaussian Splats Town Hall - Part 2](https://youtu.be/5_GaPYBHqOo)
- [Intro to gaussian splatting (and Unity plugin)](https://www.xuanprada.com/blog/2023/10/22/intro-to-gaussian-splatting)
- [Jupyter Tutorial](https://www.youtube.com/watch?v=OcvA7fmiZYM)

## Credits

- Thanks to [Leonid Keselman](https://github.com/leonidk) for informing me about the release of the paper "Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting".
- Thanks to [Eric Haines](https://github.com/erich666) for suggesting the jupyter notebook viewer, windows tutorial and for fixing text hyphenations and other issues.
- Thanks to [Henry Pearce](https://github.com/henrypearce4D) for maintaining contributions.
- [Yehe Liu](https://x.com/YeheLiu)
