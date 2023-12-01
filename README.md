# Awesome 3D Gaussian Splatting Resources 

A curated list of papers and open-source resources focused on 3D Gaussian Splatting, intended to keep pace with the anticipated surge of research in the coming months. If you have any additions or suggestions, feel free to contribute. Additional resources like blog posts, videos, etc. are also welcome.

## Table of contents

- [Seminal Paper introducing 3D Gaussian Splatting](#seminal-paper-introducing-3d-gaussian-splatting)
- [Dynamic 3D Gaussian Splatting](#dynamic-3d-gaussian-splatting)
- [Diffusion 3D Gaussian Splatting](#diffusion-3d-gaussian-splatting)
- [3D Gaussian Splatting Avatars](#3d-gaussian-splatting-avatars)
- [3D Gaussian Splatting SLAM](#3d-gaussian-splatting-slam)
- [3D Gaussian Splatting Mesh Extraction and Physics](#3d-gaussian-splatting-mesh-extraction-and-physics)
- [Regularization and Optimization](#regularization-and-optimization)
- [3D Gaussian Editing](#3d-gaussian-editing)
- [3D Gaussian Rendering](#3d-gaussian-rendering)
- [3D Gaussian Compression](#3d-gaussian-compression)
- [Misc](#misc)
- [Classic work](#classic-work)
- [Open Source Implementations](#open-source-implementations)
  * [Reference](#reference)
  * [Unofficial Implementations](#unofficial-implementations)
  * [2D Gaussian Splatting](#2d-gaussian-splatting)
  * [Game Engines](#game-engines)
  * [Viewers](#viewers)
  * [Utilities](#utilities)
- [Blog Posts](#blog-posts)
- [Tutorial Videos](#tutorial-videos)
- [Credits](#credits)


<details span>
<summary><b>Update Log:</b></summary>
<br>

 **December 1, 2023**:
  - 4 papers added: Compact3D, GaussianShader, Periodic Vibration Gaussian and Gaussian Shell Maps for Efficient 3D Human Generation.
  - Created Table of contents for each category and added line breaks.

 **November 30, 2023**:
  - Added Unreal game engine implementation.
  - 5 papers added: LightGaussian, FisherRF, HUGS, HumanGaussian, CG3D, and Multi Scale 3DGS.
  
 **November 29, 2023**:
  - Added two papers: Point and Move and IR-GS.

 **November 28, 2023**:
  - Added five papers: GaussinEditor, Relightable Gaussians, GART, Mip-Splatting, HumanGaussian.

 **November 27, 2023**:
  - Added two papers: Gaussian Editing and Compact 3D Gaussians.

 **November 25, 2023**:
  - Animatable Gaussians project added (paper not yet released).

 **November 22, 2023**:
  - 3 new GS papers added: Animatable, Depth-Regularized, and Monocular/Multi-view 3DGS.
  - Added some classic papers.
  - Added another GS paper also called LucidDreamer.

 **November 21, 2023**:
  - 3 new GS papers added: GaussianDiffusion, LucidDreamer, PhysGaussian.
  - 2 more GS papers added: SuGaR, PhysGaussian.

 **November 21, 2023**:
  - Added the paper GS-SLAM

**November 17, 2023**:
  - Added PlayCanvas implementation to Game Engines section.

 **November 16, 2023**:
  - Deformable 3D Gaussians code released.
  - Drivable 3D Gaussian Avatars paper added. 

 **November 8, 2023**:
  - Some notes about the 3DGS implementation and unsive/rsal format discussion.

 **November 4, 2023**:
  - Added 2D gaussian splatting.
  - Added very detailed (technical) blog post explaining 3D gaussian splatting.

 **October 28, 2023**:
  - Added Utilities Section.
  - Added 3DGS Converter for editing 3DGS .ply files in Cloud Compare to Utilities.
  - Added Kapture (for bundler to colmap model conversion) and Kapture image cropper script with conversion instructions to Utilities.

 **October 23, 2023**:
  - Added python WebGL viewer 2.
  - Added Intro to gaussian splatting (and Unity viewer) video blog.

  **October 21, 2023**:
  - Added python OpenGL viewer.
  - Added typescript WebGPU viewer.

  **October 20, 2023**:
  - Made abstracts readable (removed hyphenations).
  - Added Windows tutorial.
  - Other minor text fixes.
  - Added Jupyter notebook viewer.

**October 19, 2023**: 
  - Added Github page link for Real-time Photorealistic Dynamic Scene Representation.
  - Re-ordered headings.
  - Added other unofficial implementations.
  - Moved Nerfstudio gsplat and fast: C++/CUDA to Unofficial Implementations.
  - Added Nerfstudio, Blender, WebRTC, iOS & Metal viewers.

**October 17, 2023**: 
  - GaussianDreamer code released.
  - Added Real-time Photorealistic Dynamic Scene Representation.

**October 16, 2023**: 
  - Added Deformable 3D Gaussians paper.
  - Dynamic 3D Gaussians code released.
**October 15, 2023**: Initial list with first 6 papers.
</details>

<br>

## Seminal Paper introducing 3D Gaussian Splatting:
### 3D Gaussian Splatting for Real-Time Radiance Field Rendering
**Authors**: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis

<details span>
<summary><b>Abstract</b></summary>
Radiance Field methods have recently revolutionized novel-view synthesis
of scenes captured with multiple photos or videos. However, achieving high
visual quality still requires neural networks that are costly to train and render,
while recent faster methods inevitably trade off speed for quality. For
unbounded and complete scenes (rather than isolated objects) and 1080p
resolution rendering, no current method can achieve real-time display rates.
We introduce three key elements that allow us to achieve state-of-the-art
visual quality while maintaining competitive training times and importantly
allow high-quality real-time (≥ 30 fps) novel-view synthesis at 1080p resolution.
First, starting from sparse points produced during camera calibration,
we represent the scene with 3D Gaussians that preserve desirable properties
of continuous volumetric radiance fields for scene optimization while
avoiding unnecessary computation in empty space; Second, we perform
interleaved optimization/density control of the 3D Gaussians, notably optimizing
anisotropic covariance to achieve an accurate representation of the
scene; Third, we develop a fast visibility-aware rendering algorithm that
supports anisotropic splatting and both accelerates training and allows real-time
rendering. We demonstrate state-of-the-art visual quality and real-time
rendering on several established datasets.
</details>
  
  [📄 Paper (Low Resolution)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf) | [📄 Paper (High Resolution)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_high.pdf) | [🌐 Project Page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | [💻 Code](https://github.com/graphdeco-inria/gaussian-splatting) | [🎥 Short Presentation](https://youtu.be/T_kXY43VZnk?si=DrkbDFxQAv5scQNT) | [🎥 Explanation Video](https://www.youtube.com/live/xgwvU7S0K-k?si=edF8NkYtsRbgTbKi)

<br>

## Dynamic 3D Gaussian Splatting:
### 1. Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis
**Authors**: Jonathon Luiten, Georgios Kopanas, Bastian Leibe, Deva Ramanan

<details span>
<summary><b>Abstract</b></summary>
We present a method that simultaneously addresses the
tasks of dynamic scene novel-view synthesis and six degree-
of-freedom (6-DOF) tracking of all dense scene elements.
We follow an analysis-by-synthesis framework, inspired by
recent work that models scenes as a collection of 3D Gaussians
which are optimized to reconstruct input images via
differentiable rendering. To model dynamic scenes, we al-
low Gaussians to move and rotate over time while enforcing
that they have persistent color, opacity, and size. By regularizing
Gaussians’ motion and rotation with local-rigidity
constraints, we show that our Dynamic 3D Gaussians correctly
model the same area of physical space over time, including
the rotation of that space. Dense 6-DOF tracking
and dynamic reconstruction emerges naturally from persistent
dynamic view synthesis, without requiring any correspondence
or flow as input. We demonstrate a large number of
downstream applications enabled by our representation,
including first-person view synthesis, dynamic compositional
scene synthesis, and 4D video editing.
</details>

  [📄 Paper](https://dynamic3dgaussians.github.io/paper.pdf) | [🌐 Project Page](https://dynamic3dgaussians.github.io/) | [💻 Code](https://github.com/JonathonLuiten/Dynamic3DGaussians) | [🎥 Explanation Video](https://www.youtube.com/live/hDuy1TgD8I4?si=6oGN0IYnPRxOibpg)

### 2. Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction
**Authors**: Ziyi Yang, Xinyu Gao, Wen Zhou, Shaohui Jiao, Yuqing Zhang, Xiaogang Jin 

<details span>
<summary><b>Abstract</b></summary>
Implicit neural representation has opened up new avenues for dynamic scene reconstruction and rendering. Nonetheless, state-of-the-art methods of dynamic neural rendering rely heavily on these implicit representations, which frequently struggle with accurately capturing the intricate details of objects in the scene. Furthermore, implicit methods struggle to achieve real-time rendering in general dynamic scenes, limiting their use in a wide range of tasks. To address the issues, we propose a deformable 3D Gaussians Splatting method that reconstructs scenes using explicit 3D Gaussians and learns Gaussians in canonical space with a deformation field to model monocular dynamic scenes. We also introduced a smoothing training mechanism with no extra overhead to mitigate the impact of inaccurate poses in real datasets on the smoothness of time interpolation tasks. Through differential gaussian rasterization, the deformable 3D Gaussians not only achieve higher rendering quality but also real-time rendering speed. Experiments show that our method outperforms existing methods significantly in terms of both rendering quality and speed, making it well-suited for tasks such as novel-view synthesis, time synthesis, and real-time rendering. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2309.13101.pdf) | [🌐 Project Page](https://ingra14m.github.io/Deformable-Gaussians/) | [💻 Code](https://github.com/ingra14m/Deformable-3D-Gaussians) 

### 3. 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering
**Authors**: Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Tian Qi, Xinggang Wang

<details span>
<summary><b>Abstract</b></summary>
Representing and rendering dynamic scenes has been an
important but challenging task. Especially, to accurately
model complex motions, high efficiency is usually hard to
maintain. We introduce the 4D Gaussian Splatting (4D-GS)
to achieve real-time dynamic scene rendering while also
enjoying high training and storage efficiency. An efficient
deformation field is constructed to model both Gaussian
motions and shape deformations. Different adjacent Gaussians
are connected via a HexPlane to produce more accurate
position and shape deformations. Our 4D-GS method
achieves real-time rendering under high resolutions, 70
FPS at a 800×800 resolution on an RTX 3090 GPU, while
maintaining comparable or higher quality than previous
state-of-the-art method.
</details>

  [📄 Paper](https://arxiv.org/pdf/2310.08528.pdf) | [🌐 Project Page](https://guanjunwu.github.io/4dgs/) | [💻 Code](https://github.com/hustvl/4DGaussians)
  
### 4. Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting

<details span>
<summary><b>Abstract</b></summary>
Reconstructing dynamic 3D scenes from 2D images and generating diverse views over time is challenging due to scene complexity and temporal dynamics. Despite advancements in neural implicit models, limitations persist: (i) Inadequate Scene Structure: Existing methods struggle to reveal the spatial and temporal structure of dynamic scenes from directly learning the complex 6D plenoptic function. (ii) Scaling Deformation Modeling: Explicitly modeling scene element deformation becomes impractical for complex dynamics. To address these issues, we consider the spacetime as an entirety and propose to approximate the underlying spatio-temporal 4D volume of a dynamic scene by optimizing a collection of 4D primitives, with explicit geometry and appearance modeling. Learning to optimize the 4D primitives enables us to synthesize novel views at any desired time with our tailored rendering routine. Our model is conceptually simple, consisting of a 4D Gaussian parameterized by anisotropic ellipses that can rotate arbitrarily in space and time, as well as view-dependent and time-evolved appearance represented by the coefficient of 4D spherindrical harmonics. This approach offers simplicity, flexibility for variable-length video and end-to-end training, and efficient real-time rendering, making it suitable for capturing complex dynamic scene motions. Experiments across various benchmarks, including monocular and multi-view scenarios, demonstrate our 4DGS model's superior visual quality and efficiency. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2310.10642.pdf) | [💻 Code (to be released)](https://github.com/fudan-zvg/4d-gaussian-splatting) 

### 5. An Efficient 3D Gaussian Representation for Monocular/Multi-view Dynamic Scenes 
**Authors**: Kai Katsumata, Duc Minh Vo, Hideki Nakayama 

<details span>
<summary><b>Abstract</b></summary>
In novel view synthesis of scenes from multiple input views, 3D Gaussian splatting emerges as a viable alternative to existing radiance field approaches, delivering great visual quality and real-time rendering. While successful in static scenes, the present advancement of 3D Gaussian representation, however, faces challenges in dynamic scenes in terms of memory consumption and the need for numerous observations per time step, due to the onus of storing 3D Gaussian parameters per time step. In this study, we present an efficient 3D Gaussian representation tailored for dynamic scenes in which we define positions and rotations as functions of time while leaving other time-invariant properties of the static 3D Gaussian unchanged. Notably, our representation reduces memory usage, which is consistent regardless of the input sequence length. Additionally, it mitigates the risk of overfitting observed frames by accounting for temporal changes. The optimization of our Gaussian representation based on image and flow reconstruction results in a powerful framework for dynamic scene view synthesis in both monocular and multi-view cases. We obtain the highest rendering speed of 118 frames per second (FPS) at a resolution of 1352×1014 with a single GPU, showing the practical usability and effectiveness of our proposed method in dynamic scene rendering scenarios
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.12897.pdf) 

<br>

## Diffusion 3D Gaussian Splatting:

### 1. Text-to-3D using Gaussian Splatting
**Authors**: Zilong Chen, Feng Wang, Huaping Liu

<details span>
<summary><b>Abstract</b></summary>
In this paper, we present Gaussian Splatting based text-to-3D generation (GSGEN),
a novel approach for generating high-quality 3D objects. Previous methods suffer
from inaccurate geometry and limited fidelity due to the absence of 3D prior and
proper representation. We leverage 3D Gaussian Splatting, a recent state-of-the-art
representation, to address existing shortcomings by exploiting the explicit nature
that enables the incorporation of 3D prior. Specifically, our method adopts a pro-
gressive optimization strategy, which includes a geometry optimization stage and an
appearance refinement stage. In geometry optimization, a coarse representation is
established under a 3D geometry prior along with the ordinary 2D SDS loss, ensuring
a sensible and 3D-consistent rough shape. Subsequently, the obtained Gaussians
undergo an iterative refinement to enrich details. In this stage, we increase the number
of Gaussians by compactness-based densification to enhance continuity and
improve fidelity. With these designs, our approach can generate 3D content with
delicate details and more accurate geometry. Extensive evaluations demonstrate the
effectiveness of our method, especially for capturing high-frequency components.
</details>

[📄 Paper](https://arxiv.org/pdf/2309.16585.pdf) | [🌐 Project Page](https://gsgen3d.github.io/) | [💻 Code](https://github.com/gsgen3d/gsgen) | [🎥 Short Presentation](https://streamable.com/28snte) | [🎥 Explanation Video](https://www.youtube.com/live/l956ye13F8M?si=ZkvFL_lsY5OQUB7e)

### 2. DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation
**Authors**: Jiaxiang Tang, Jiawei Ren, Hang Zhou, Ziwei Liu, Gang Zeng

<details span>
<summary><b>Abstract</b></summary>
Recent advances in 3D content creation mostly leverage optimization-based 3D
generation via score distillation sampling (SDS). Though promising results have
been exhibited, these methods often suffer from slow per-sample optimization,
limiting their practical usage. In this paper, we propose DreamGaussian, a novel
3D content generation framework that achieves both efficiency and quality simultaneously.
Our key insight is to design a generative 3D Gaussian Splatting model
with companioned mesh extraction and texture refinement in UV space. In contrast
to the occupancy pruning used in Neural Radiance Fields, we demonstrate
that the progressive densification of 3D Gaussians converges significantly faster
for 3D generative tasks. To further enhance the texture quality and facilitate downstream
applications, we introduce an efficient algorithm to convert 3D Gaussians
into textured meshes and apply a fine-tuning stage to refine the details. Extensive
experiments demonstrate the superior efficiency and competitive generation
quality of our proposed approach. Notably, DreamGaussian produces high-quality
textured meshes in just 2 minutes from a single-view image, achieving approximately
10 times acceleration compared to existing methods.
</details>

  [📄 Paper](https://arxiv.org/pdf/2309.16653.pdf) | [🌐 Project Page](https://dreamgaussian.github.io/) | [💻 Code](https://github.com/dreamgaussian/dreamgaussian) | [🎥 Explanation Video](https://www.youtube.com/live/l956ye13F8M?si=ZkvFL_lsY5OQUB7e)

### 3. GaussianDreamer: Fast Generation from Text to 3D Gaussian Splatting with Point Cloud Priors
**Authors**:  Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,
Wenyu Liu, Tian Qi, Xinggang Wang 
<details span>
<summary><b>Abstract</b></summary>
In recent times, the generation of 3D assets from text
prompts has shown impressive results. Both 2D and 3D
diffusion models can generate decent 3D objects based on
prompts. 3D diffusion models have good 3D consistency,
but their quality and generalization are limited as trainable 
3D data is expensive and hard to obtain. 2D diffusion models enjoy strong abilities of generalization and
fine generation, but the 3D consistency is hard to guarantee. This paper attempts to bridge the power from the two
types of diffusion models via the recent explicit and efficient
3D Gaussian splatting representation. A fast 3D generation framework, named as GaussianDreamer, is proposed,
where the 3D diffusion model provides point cloud priors
for initialization and the 2D diffusion model enriches the
geometry and appearance. Operations of noisy point growing and color perturbation are introduced to enhance the
initialized Gaussians. Our GaussianDreamer can generate a high-quality 3D instance within 25 minutes on one
GPU, much faster than previous methods, while the generated instances can be directly rendered in real time.
</details>

  [📄 Paper](https://arxiv.org/pdf/2310.08529.pdf) | [🌐 Project Page](https://taoranyi.com/gaussiandreamer/) | [💻 Code](https://github.com/hustvl/GaussianDreamer) 

### 4. GaussianDiffusion: 3D Gaussian Splatting for Denoising Diffusion Probabilistic Models with Structured Noise  
 Xinhai Li, Huaibin Wang, Kuo-Kun Tseng
<details span>
<summary><b>Abstract</b></summary>
 Text-to-3D, known for its efficient generation methods and expansive creative potential, has garnered significant attention in the AIGC domain. However, the amalgamation of Nerf and 2D diffusion models frequently yields oversaturated images, posing severe limitations on downstream industrial applications due to the constraints of pixelwise rendering method. Gaussian splatting has recently superseded the traditional pointwise sampling technique prevalent in NeRF-based methodologies, revolutionizing various aspects of 3D reconstruction. This paper introduces a novel text to 3D content generation framework based on Gaussian splatting, enabling fine control over image saturation through individual Gaussian sphere transparencies, thereby producing more realistic images. The challenge of achieving multi-view consistency in 3D generation significantly impedes modeling complexity and accuracy. Taking inspiration from SJC, we explore employing multi-view noise distributions to perturb images generated by 3D Gaussian splatting, aiming to rectify inconsistencies in multi-view geometry. We ingeniously devise an efficient method to generate noise that produces Gaussian noise from diverse viewpoints, all originating from a shared noise source. Furthermore, vanilla 3D Gaussian-based generation tends to trap models in local minima, causing artifacts like floaters, burrs, or proliferative elements. To mitigate these issues, we propose the variational Gaussian splatting technique to enhance the quality and stability of 3D appearance. To our knowledge, our approach represents the first comprehensive utilization of Gaussian splatting across the entire spectrum of 3D content generation processes.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.11221.pdf)  

### 5. LucidDreamer: Towards High-Fidelity Text-to-3D Generation via Interval Score Matching  
Yixun Liang, Xin Yang, Jiantao Lin, Haodong Li, Xiaogang Xu, Yingcong Chen
<details span>
<summary><b>Abstract</b></summary>
The recent advancements in text-to-3D generation mark a significant milestone in generative models, unlocking new possibilities for creating imaginative 3D assets across various real-world scenarios. While recent advancements in text-to-3D generation have shown promise, they often fall short in rendering detailed and high-quality 3D models. This problem is especially prevalent as many methods base themselves on Score Distillation Sampling (SDS). This paper identifies a notable deficiency in SDS, that it brings inconsistent and low-quality updating direction for the 3D model, causing the over-smoothing effect. To address this, we propose a novel approach called Interval Score Matching (ISM). ISM employs deterministic diffusing trajectories and utilizes interval-based score matching to counteract over-smoothing. Furthermore, we incorporate 3D Gaussian Splatting into our text-to-3D generation pipeline. Extensive experiments show that our model largely outperforms the state-of-the-art in quality and training efficiency.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.11284.pdf) | [💻 Code](https://github.com/EnVision-Research/LucidDreamer) 

### 6. LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes
Jaeyoung Chung, Suyoung Lee, Hyeongjin Nam, Jaerin Lee, Kyoung Mu Lee
<details span>
<summary><b>Abstract</b></summary>
With the widespread usage of VR devices and contents, demands for 3D scene generation techniques become more popular. Existing 3D scene generation models, however, limit the target scene to specific domain, primarily due to their training strategies using 3D scan dataset that is far from the real-world. To address such limitation, we propose LucidDreamer, a domain-free scene generation pipeline by fully leveraging the power of existing large-scale diffusion-based generative model. Our LucidDreamer has two alternate steps: Dreaming and Alignment. First, to generate multi-view consistent images from inputs, we set the point cloud as a geometrical guideline for each image generation. Specifically, we project a portion of point cloud to the desired view and provide the projection as a guidance for inpainting using the generative model. The inpainted images are lifted to 3D space with estimated depth maps, composing a new points. Second, to aggregate the new points into the 3D scene, we propose an aligning algorithm which harmoniously integrates the portions of newly generated 3D scenes. The finally obtained 3D scene serves as initial points for optimizing Gaussian splats. LucidDreamer produces Gaussian splats that are highly-detailed compared to the previous 3D scene generation methods, with no constraint on domain of the target scene. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.13384.pdf) | [🌐 Project Page](https://luciddreamer-cvlab.github.io/) | [💻 Code (not yet)](https://github.com/anonymous-luciddreamer/LucidDreamer) 

### 7. HumanGaussian: Text-Driven 3D Human Generation with Gaussian Splatting  
Xian Liu, Xiaohang Zhan, Jiaxiang Tang, Ying Shan, Gang Zeng, Dahua Lin, Xihui Liu, Ziwei Liu
<details span>
<summary><b>Abstract</b></summary>
Realistic 3D human generation from text prompts is a desirable yet challenging task. Existing methods optimize 3D representations like mesh or neural fields via score distillation sampling (SDS), which suffers from inadequate fine details or excessive training time. In this paper, we propose an efficient yet effective framework, HumanGaussian, that generates high-quality 3D humans with fine-grained geometry and realistic appearance. Our key insight is that 3D Gaussian Splatting is an efficient renderer with periodic Gaussian shrinkage or growing, where such adaptive density control can be naturally guided by intrinsic human structures. Specifically, 1) we first propose a Structure-Aware SDS that simultaneously optimizes human appearance and geometry. The multi-modal score function from both RGB and depth space is leveraged to distill the Gaussian densification and pruning process. 2) Moreover, we devise an Annealed Negative Prompt Guidance by decomposing SDS into a noisier generative score and a cleaner classifier score, which well addresses the over-saturation issue. The floating artifacts are further eliminated based on Gaussian size in a prune-only phase to enhance generation smoothness. Extensive experiments demonstrate the superior efficiency and competitive quality of our framework, rendering vivid 3D humans under diverse scenarios.
</details>

  [📄 Paper](https://alvinliu0.github.io/projects/HumanGaussian/humangaussian.pdf) | [🌐 Project Page](https://alvinliu0.github.io/projects/HumanGaussian) | [💻 Code](https://github.com/alvinliu0/HumanGaussian) | [🎥 Short Presentation](https://www.youtube.com/watch?v=S3djzHoqPKY)

### 8. CG3D: Compositional Generation for Text-to-3D
Alexander Vilesov, Pradyumna Chari, Achuta Kadambi
<details span>
<summary><b>Abstract</b></summary>
With the onset of diffusion-based generative models and their ability to generate text-conditioned images, content generation has received a massive invigoration. Recently, these models have been shown to provide useful guidance for the generation of 3D graphics assets. However, existing work in text-conditioned 3D generation faces fundamental constraints: (i) inability to generate detailed, multi-object scenes, (ii) inability to textually control multi-object configurations, and (iii) physically realistic scene composition. In this work, we propose CG3D, a method for compositionally generating scalable 3D assets that resolves these constraints. We find that explicit Gaussian radiance fields, parameterized to allow for compositions of objects, possess the capability to enable semantically and physically consistent scenes. By utilizing a guidance framework built around this explicit representation, we show state of the art results, capable of even exceeding the guiding diffusion model in terms of object combinations and physics accuracy.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.17907.pdf) | [🌐 Project Page](https://asvilesov.github.io/CG3D/) | | [🎥 Short Presentation](https://www.youtube.com/watch?v=FMAVeolsE7s)

### 9. 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering
Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Qi Tian, Xinggang Wang
<details span>
<summary><b>Abstract</b></summary>
 Representing and rendering dynamic scenes has been an important but challenging task. Especially, to accurately model complex motions, high efficiency is usually hard to maintain. We introduce the 4D Gaussian Splatting (4D-GS) to achieve real-time dynamic scene 
 rendering while also enjoying high training and storage efficiency. An efficient deformation field is constructed to model both Gaussian motions and shape deformations. Different adjacent Gaussians are connected via a HexPlane to produce more accurate position and 
 shape deformations. Our 4D-GS method achieves real-time rendering under high resolutions, 70 FPS at an 800×800 resolution on an RTX 3090 GPU, while maintaining comparable or higher quality than previous state-of-the-art methods. More demos and code are available at https://guanjunwu.github.io/4dgs/.
 </details>
 [📄 Paper](https://arxiv.org/pdf/2310.08528.pdf) | [🌐 Project Page](https://guanjunwu.github.io/4dgs/) | | [💻 Code](https://github.com/hustvl/4DGaussians)

 ### 10. Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction
 Ziyi Yang, Xinyu Gao, Wen Zhou, Shaohui Jiao, Yuqing Zhang, Xiaogang Jin
<details span>
<summary><b>Abstract</b></summary>
Implicit neural representation has opened up new avenues for dynamic scene reconstruction and rendering. Nonetheless, state-of-the-art methods of dynamic neural rendering rely heavily on these implicit representations, which frequently struggle with accurately capturing the intricate details of objects in the scene. Furthermore, implicit methods struggle to achieve real-time rendering in general dynamic scenes, limiting their use in a wide range of tasks. To address the issues, we propose a deformable 3D Gaussians Splatting method that reconstructs scenes using explicit 3D Gaussians and learns Gaussians in canonical space with a deformation field to model monocular dynamic scenes. We also introduced a smoothing training mechanism with no extra overhead to mitigate the impact of inaccurate poses in real datasets on the smoothness of time interpolation tasks. Through differential gaussian rasterization, the deformable 3D Gaussians not only achieve higher rendering quality but also real-time rendering speed. Experiments show that our method outperforms existing methods significantly in terms of both rendering quality and speed, making it well-suited for tasks such as novel-view synthesis, time synthesis, and real-time rendering. We plan to release our code and data soon.
</details>
 [📄 Paper](https://arxiv.org/pdf/2309.13101.pdf) | [🌐 Project Page](https://ingra14m.github.io/Deformable-Gaussians/) | | [💻 Code](https://github.com/ingra14m/Deformable-3D-Gaussians)

<br>

## 3D Gaussian Splatting Avatars:
### 1. Drivable 3D Gaussian Avatars 
**Authors**:  Wojciech Zielonka, Timur Bagautdinov, Shunsuke Saito, Michael Zollhöfer, Justus Thies, Javier Romero
<details span>
<summary><b>Abstract</b></summary>
We present Drivable 3D Gaussian Avatars (D3GA), the
first 3D controllable model for human bodies rendered with
Gaussian splats. Current photorealistic drivable avatars
require either accurate 3D registrations during training,
dense input images during testing, or both. The ones based
on neural radiance fields also tend to be prohibitively slow
for telepresence applications. This work uses the recently
presented 3D Gaussian Splatting (3DGS) technique to render realistic humans at real-time framerates, using dense
calibrated multi-view videos as input. To deform those
primitives, we depart from the commonly used point deformation method of linear blend skinning (LBS) and use
a classic volumetric deformation method: cage deformations. Given their smaller size, we drive these deformations
with joint angles and keypoints, which are more suitable for
communication applications. Our experiments on nine subjects with varied body shapes, clothes, and motions obtain
higher-quality results than state-of-the-art methods when
using the same training and test data.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.08581.pdf) | [🌐 Project Page](https://zielon.github.io/d3ga/) | | [🎥 Short Presentation](https://youtu.be/C4IT1gnkaF0?si=zUJLm8adM68pVvR8) 

### 2. SplatArmor: Articulated Gaussian splatting for animatable humans from monocular RGB videos 
**Authors**: Rohit Jena, Ganesh Subramanian Iyer, Siddharth Choudhary, Brandon Smith, Pratik Chaudhari, James Gee 
<details span>
<summary><b>Abstract</b></summary>
We propose SplatArmor, a novel approach for recovering detailed and animatable human models by `armoring' a parameterized body model with 3D Gaussians. Our approach represents the human as a set of 3D Gaussians within a canonical space, whose articulation is defined by extending the skinning of the underlying SMPL geometry to arbitrary locations in the canonical space. To account for pose-dependent effects, we introduce a SE(3) field, which allows us to capture both the location and anisotropy of the Gaussians. Furthermore, we propose the use of a neural color field to provide color regularization and 3D supervision for the precise positioning of these Gaussians. We show that Gaussian splatting provides an interesting alternative to neural rendering based methods by leverging a rasterization primitive without facing any of the non-differentiability and optimization challenges typically faced in such approaches. The rasterization paradigms allows us to leverage forward skinning, and does not suffer from the ambiguities associated with inverse skinning and warping. We show compelling results on the ZJU MoCap and People Snapshot datasets, which underscore the effectiveness of our method for controllable human synthesis.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.10812.pdf) |  [🌐 Project Page](https://jenaroh.it/splatarmor/) | [💻 Code (not yet)](https://github.com/rohitrango/splatarmor)

### 3. Animatable 3D Gaussians for High-fidelity Synthesis of Human Motions 
**Authors**: Keyang Ye, Tianjia Shao, Kun Zhou 
<details span>
<summary><b>Abstract</b></summary>
We present a novel animatable 3D Gaussian model for rendering high-fidelity free-view human motions in real time. Compared to existing NeRF-based methods, the model owns better capability in synthesizing high-frequency details without the jittering problem across video frames. The core of our model is a novel augmented 3D Gaussian representation, which attaches each Gaussian with a learnable code. The learnable code serves as a pose-dependent appearance embedding for refining the erroneous appearance caused by geometric transformation of Gaussians, based on which an appearance refinement model is learned to produce residual Gaussian properties to match the appearance in target pose. To force the Gaussians to learn the foreground human only without background interference, we further design a novel alpha loss to explicitly constrain the Gaussians within the human body. We also propose to jointly optimize the human joint parameters to improve the appearance accuracy. The animatable 3D Gaussian model can be learned with shallow MLPs, so new human motions can be synthesized in real time (66 fps on avarage). Experiments show that our model has superior performance over NeRF-based methods. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.13404.pdf) 
  
### 4. Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling 
**Authors**: Zhe Li, Zerong Zheng, Lizhen Wang, Yebin Liu 
<details span>
<summary><b>Abstract</b></summary>
Modeling animatable human avatars from RGB videos is a long-standing and challenging problem. Recent works usually adopt MLP-based neural radiance fields (NeRF) to represent 3D humans, but it remains difficult for pure MLPs to regress pose-dependent garment details. To this end, we introduce Animatable Gaussians, a new avatar representation that leverages powerful 2D CNNs and 3D Gaussian splatting to create high-fidelity avatars. To associate 3D Gaussians with the animatable avatar, we learn a parametric template from the input videos, and then parameterize the template on two front & back canonical Gaussian maps where each pixel represents a 3D Gaussian. The learned template is adaptive to the wearing garments for modeling looser clothes like dresses. Such template-guided 2D parameterization enables us to employ a powerful StyleGAN-based CNN to learn the pose-dependent Gaussian maps for modeling detailed dynamic appearances. Furthermore, we introduce a pose projection strategy for better generalization given novel poses. Overall, our method can create lifelike avatars with dynamic, realistic and generalized appearances. Experiments show that our method outperforms other state-of-the-art approaches. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.16096.pdf) | [🌐 Project Page](https://animatable-gaussians.github.io/) | [💻 Code (not yet)](https://github.com/lizhe00/AnimatableGaussians)

### 5. GART: Gaussian Articulated Template Models 
**Authors**: Jiahui Lei, Yufu Wang, Georgios Pavlakos, Lingjie Liu, Kostas Daniilidis 
<details span>
<summary><b>Abstract</b></summary>
We introduce Gaussian Articulated Template Model GART, an explicit, efficient, and expressive representation for non-rigid articulated subject capturing and rendering from monocular videos. GART utilizes a mixture of moving 3D Gaussians to explicitly approximate a deformable subject's geometry and appearance. It takes advantage of a categorical template model prior (SMPL, SMAL, etc.) with learnable forward skinning while further generalizing to more complex non-rigid deformations with novel latent bones. GART can be reconstructed via differentiable rendering from monocular videos in seconds or minutes and rendered in novel poses faster than 150fps.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.16099.pdf) | [🌐 Project Page](https://www.cis.upenn.edu/~leijh/projects/gart/) | [💻 Code](https://github.com/JiahuiLei/GART) | [🎥 Short Presentation](https://www.youtube.com/watch?v=-xYNtIlW4WY)

### 6. Human Gaussian Splatting: Real-time Rendering of Animatable Avatars 
**Authors**: Arthur Moreau, Jifei Song, Helisa Dhamo, Richard Shaw, Yiren Zhou, Eduardo Pérez-Pellitero 
<details span>
<summary><b>Abstract</b></summary>
This work addresses the problem of real-time rendering of photorealistic human body avatars learned from multi-view videos. While the classical approaches to model and render virtual humans generally use a textured mesh, recent research has developed neural body representations that achieve impressive visual quality. However, these models are difficult to render in real-time and their quality degrades when the character is animated with body poses different than the training observations. We propose the first animatable human model based on 3D Gaussian Splatting, that has recently emerged as a very efficient alternative to neural radiance fields. Our body is represented by a set of gaussian primitives in a canonical space which are deformed in a coarse to fine approach that combines forward skinning and local non-rigid refinement. We describe how to learn our Human Gaussian Splatting (\OURS) model in an end-to-end fashion from multi-view observations, and evaluate it against the state-of-the-art approaches for novel pose synthesis of clothed body. Our method presents a PSNR 1.5dbB better than the state-of-the-art on THuman4 dataset while being able to render at 20fps or more. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.17113.pdf) 

### 7. HUGS: Human Gaussian Splats 
**Authors**: Muhammed Kocabas, Jen-Hao Rick Chang, James Gabriel, Oncel Tuzel, Anurag Ranjan 
<details span>
<summary><b>Abstract</b></summary>
Recent advances in neural rendering have improved both training and rendering times by orders of magnitude. While these methods demonstrate state-of-the-art quality and speed, they are designed for photogrammetry of static scenes and do not generalize well to freely moving humans in the environment. In this work, we introduce Human Gaussian Splats (HUGS) that represents an animatable human together with the scene using 3D Gaussian Splatting (3DGS). Our method takes only a monocular video with a small number of (50-100) frames, and it automatically learns to disentangle the static scene and a fully animatable human avatar within 30 minutes. We utilize the SMPL body model to initialize the human Gaussians. To capture details that are not modeled by SMPL (e.g. cloth, hairs), we allow the 3D Gaussians to deviate from the human body model. Utilizing 3D Gaussians for animated humans brings new challenges, including the artifacts created when articulating the Gaussians. We propose to jointly optimize the linear blend skinning weights to coordinate the movements of individual Gaussians during animation. Our approach enables novel-pose synthesis of human and novel view synthesis of both the human and the scene. We achieve state-of-the-art rendering quality with a rendering speed of 60 FPS while being ~100x faster to train over previous work.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.17910.pdf)

### 8. Gaussian Shell Maps for Efficient 3D Human Generation
**Authors**: Rameen Abdal, Wang Yifan, Zifan Shi, Yinghao Xu, Ryan Po, Zhengfei Kuang, Qifeng Chen, Dit-Yan Yeung, Gordon Wetzstein
<details span>
<summary><b>Abstract</b></summary>
Efficient generation of 3D digital humans is important in several industries, including virtual reality, social media, and cinematic production. 3D generative adversarial networks (GANs) have demonstrated state-of-the-art (SOTA) quality and diversity for generated assets. Current 3D GAN architectures, however, typically rely on volume representations, which are slow to render, thereby hampering the GAN training and requiring multi-view-inconsistent 2D upsamplers. Here, we introduce Gaussian Shell Maps (GSMs) as a framework that connects SOTA generator network architectures with emerging 3D Gaussian rendering primitives using an articulable multi shell–based scaffold. In this setting, a CNN generates a 3D texture stack with features that are mapped to the shells. The latter represent inflated and deflated versions of a template surface of a digital human in a canonical body pose. Instead of rasterizing the shells directly, we sample 3D Gaussians on the shells whose attributes are encoded in the texture features. These Gaussians are efficiently and differentiably rendered. The ability to articulate the shells is important during GAN training and, at inference time, to deform a body into arbitrary userdefined poses. Our efficient rendering scheme bypasses the need for view-inconsistent upsamplers and achieves highquality multi-view consistent renderings at a native resolution of 512 × 512 pixels. We demonstrate that GSMs successfully generate 3D humans when trained on single-view datasets, including SHHQ and DeepFashion.
</details>

  [📄 Paper](https://arxiv.org/abs/2311.17857) | [🌐 Project Page](https://rameenabdal.github.io/GaussianShellMaps/) | [💻 Code (not yet)](https://github.com/computational-imaging/GSM)

<br>

## 3D Gaussian Splatting SLAM:
### 1. GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting 
**Authors**: Chi Yan, Delin Qu, Dong Wang, Dan Xu, Zhigang Wang, Bin Zhao, Xuelong Li
<details span>
<summary><b>Abstract</b></summary>
In this paper, we introduce GS-SLAM that first utilizes 3D Gaussian representation in the Simultaneous Localization and Mapping (SLAM) system. It facilitates a better balance between efficiency and accuracy. Compared to recent SLAM methods employing neural implicit representations, our method utilizes a real-time differentiable splatting rendering pipeline that offers significant speedup to map optimization and RGB-D re-rendering. Specifically, we propose an adaptive expansion strategy that adds new or deletes noisy 3D Gaussian in order to efficiently reconstruct new observed scene geometry and improve the mapping of previously observed areas. This strategy is essential to extend 3D Gaussian representation to reconstruct the whole scene rather than synthesize a static object in existing methods. Moreover, in the pose tracking process, an effective coarse-to-fine technique is designed to select reliable 3D Gaussian representations to optimize camera pose, resulting in runtime reduction and robust estimation. Our method achieves competitive performance compared with existing state-of-the-art real-time methods on the Replica, TUM-RGBD datasets. The source code will be released upon acceptance. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.11700.pdf) 

## 3D Gaussian Splatting Mesh Extraction and Physics:
### 1. PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics
**Authors**: Tianyi Xie, Zeshun Zong, Yuxin Qiu, Xuan Li, Yutao Feng, Yin Yang, Chenfanfu Jiang
<details span>
<summary><b>Abstract</b></summary>
We introduce PhysGaussian, a new method that seamlessly integrates physically grounded Newtonian dynamics within 3D Gaussians to achieve high-quality novel motion synthesis. Employing a custom Material Point Method (MPM), our approach enriches 3D Gaussian kernels with physically meaningful kinematic deformation and mechanical stress attributes, all evolved in line with continuum mechanics principles. A defining characteristic of our method is the seamless integration between physical simulation and visual rendering: both components utilize the same 3D Gaussian kernels as their discrete representations. This negates the necessity for triangle/tetrahedron meshing, marching cubes, "cage meshes," or any other geometry embedding, highlighting the principle of "what you see is what you simulate (WS2)." Our method demonstrates exceptional versatility across a wide variety of materials--including elastic entities, metals, non-Newtonian fluids, and granular materials--showcasing its strong capabilities in creating diverse visual content with novel viewpoints and movements. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.12198.pdf) | [🌐 Project Page](https://xpandora.github.io/PhysGaussian/) | [💻 Code (not released yet)](https://github.com/XPandora/PhysGaussian) | [🎥 Short Presentation](https://drive.google.com/file/d/1eh7vxRxer7gfvPhs8jDE56oRjayBc9oe/view)

### 2. SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering 
**Authors**: Antoine Guédon, Vincent Lepetit
<details span>
<summary><b>Abstract</b></summary>
We propose a method to allow precise and extremely fast mesh extraction from 3D Gaussian Splatting. Gaussian Splatting has recently become very popular as it yields realistic rendering while being significantly faster to train than NeRFs. It is however challenging to extract a mesh from the millions of tiny 3D gaussians as these gaussians tend to be unorganized after optimization and no method has been proposed so far. Our first key contribution is a regularization term that encourages the gaussians to align well with the surface of the scene. We then introduce a method that exploits this alignment to sample points on the real surface of the scene and extract a mesh from the Gaussians using Poisson reconstruction, which is fast, scalable, and preserves details, in contrast to the Marching Cubes algorithm usually applied to extract meshes from Neural SDFs. Finally, we introduce an optional refinement strategy that binds gaussians to the surface of the mesh, and jointly optimizes these Gaussians and the mesh through Gaussian splatting rendering. This enables easy editing, sculpting, rigging, animating, compositing and relighting of the Gaussians using traditional softwares by manipulating the mesh instead of the gaussians themselves. Retrieving such an editable mesh for realistic rendering is done within minutes with our method, compared to hours with the state-of-the-art methods on neural SDFs, while providing a better rendering quality. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.12775.pdf) | [🌐 Project Page](https://imagine.enpc.fr/~guedona/sugar/) | [💻 Code (not released yet)](https://github.com/Anttwo/SuGaR) 

<br>

## Regularization and Optimization:
### 1. Depth-Regularized Optimization for 3D Gaussian Splatting in Few-Shot Images 
**Authors**: Jaeyoung Chung, Jeongtaek Oh, Kyoung Mu Lee 
<details span>
<summary><b>Abstract</b></summary>
In this paper, we present a method to optimize Gaussian splatting with a limited number of images while avoiding overfitting. Representing a 3D scene by combining numerous Gaussian splats has yielded outstanding visual quality. However, it tends to overfit the training views when only a small number of images are available. To address this issue, we introduce a dense depth map as a geometry guide to mitigate overfitting. We obtained the depth map using a pre-trained monocular depth estimation model and aligning the scale and offset using sparse COLMAP feature points. The adjusted depth aids in the color-based optimization of 3D Gaussian splatting, mitigating floating artifacts, and ensuring adherence to geometric constraints. We verify the proposed method on the NeRF-LLFF dataset with varying numbers of few images. Our approach demonstrates robust geometry compared to the original method that relies solely on images. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.13398.pdf) 

### 2. Compact 3D Gaussian Representation for Radiance Field 
**Authors**: Joo Chan Lee, Daniel Rho, Xiangyu Sun, Jong Hwan Ko, Eunbyung Park 
<details span>
<summary><b>Abstract</b></summary>
Neural Radiance Fields (NeRFs) have demonstrated remarkable potential in capturing complex 3D scenes with high fidelity. However, one persistent challenge that hinders the widespread adoption of NeRFs is the computational bottleneck due to the volumetric rendering. On the other hand, 3D Gaussian splatting (3DGS) has recently emerged as an alternative representation that leverages a 3D Gaussisan-based representation and adopts the rasterization pipeline to render the images rather than volumetric rendering, achieving very fast rendering speed and promising image quality. However, a significant drawback arises as 3DGS entails a substantial number of 3D Gaussians to maintain the high fidelity of the rendered images, which requires a large amount of memory and storage. To address this critical issue, we place a specific emphasis on two key objectives: reducing the number of Gaussian points without sacrificing performance and compressing the Gaussian attributes, such as view-dependent color and covariance. To this end, we propose a learnable mask strategy that significantly reduces the number of Gaussians while preserving high performance. In addition, we propose a compact but effective representation of view-dependent color by employing a grid-based neural field rather than relying on spherical harmonics. Finally, we learn codebooks to compactly represent the geometric attributes of Gaussian by vector quantization. In our extensive experiments, we consistently show over 10× reduced storage and enhanced rendering speed, while maintaining the quality of the scene representation, compared to 3DGS. Our work provides a comprehensive framework for 3D scene representation, achieving high performance, fast training, compactness, and real-time rendering.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.13681.pdf) | [🌐 Project Page](https://maincold2.github.io/c3dgs/) | [💻 Code ](https://github.com/maincold2/Compact-3DGS) 

<br>

## 3D Gaussian Editing:
### 1. GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting 
**Authors**: Yiwen Chen, Zilong Chen, Chi Zhang, Feng Wang, Xiaofeng Yang, Yikai Wang, Zhongang Cai, Lei Yang, Huaping Liu, Guosheng Lin
<details span>
<summary><b>Abstract</b></summary>
3D editing plays a crucial role in many areas such as gaming and virtual reality. Traditional 3D editing methods, which rely on representations like meshes and point clouds, often fall short in realistically depicting complex scenes.
On the other hand, methods based on implicit 3D representations, like Neural Radiance Field (NeRF), render complex scenes effectively but suffer from slow processing speeds and limited control over specific scene areas. In response to these challenges, our paper presents GaussianEditor, an innovative and efficient 3D editing algorithm based on Gaussian Splatting (GS), a novel 3D representation technique.
GaussianEditor enhances precision and control in editing through our proposed Gaussian Semantic Tracing, which traces the editing target throughout the training process. Additionally, we propose hierarchical Gaussian splatting (HGS) to achieve stabilized and fine results under stochastic generative guidance from 2D diffusion models. We also develop editing strategies for efficient object removal and integration, a challenging task for existing methods. Our comprehensive experiments demonstrate GaussianEditor's superior control, efficacy, and rapid performance, marking a significant advancement in 3D editing.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.14521.pdf) | [🌐 Project Page](https://buaacyw.github.io/gaussian-editor/) | [💻 Code](https://github.com/buaacyw/GaussianEditor) | [🎥 Short Presentation](https://youtu.be/TdZIICSFqsU?si=-U4tyOvaAPqIROYn)

### 2. GaussianEditor: Editing 3D Gaussians Delicately with Text Instructions 
**Authors**: Jiemin Fang, Junjie Wang, Xiaopeng Zhang, Lingxi Xie, Qi Tian 
<details span>
<summary><b>Abstract</b></summary>
Recently, impressive results have been achieved in 3D scene editing with text instructions based on a 2D diffusion model. However, current diffusion models primarily generate images by predicting noise in the latent space, and the editing is usually applied to the whole image, which makes it challenging to perform delicate, especially localized, editing for 3D scenes. Inspired by recent 3D Gaussian splatting, we propose a systematic framework, named GaussianEditor, to edit 3D scenes delicately via 3D Gaussians with text instructions. Benefiting from the explicit property of 3D Gaussians, we design a series of techniques to achieve delicate editing. Specifically, we first extract the region of interest (RoI) corresponding to the text instruction, aligning it to 3D Gaussians. The Gaussian RoI is further used to control the editing process. Our framework can achieve more delicate and precise editing of 3D scenes than previous methods while enjoying much faster training speed, i.e. within 20 minutes on a single V100 GPU, more than twice as fast as Instruct-NeRF2NeRF (45 minutes -- 2 hours)
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.14521.pdf) | [🌐 Project Page](https://gaussianeditor.github.io/) | [💻 Code (not yet)]() | [🎥 Short Presentation](https://youtu.be/KWtALsigR3k?si=h6-A44brd5rm3_CM)

### 3. Point'n Move: Interactive Scene Object Manipulation on Gaussian Splatting Radiance Fields 
**Authors**: Jiajun Huang, Hongchuan Yu 
<details span>
<summary><b>Abstract</b></summary>
We propose Point'n Move, a method that achieves interactive scene object manipulation with exposed region inpainting. Interactivity here further comes from intuitive object selection and real-time editing. To achieve this, we adopt Gaussian Splatting Radiance Field as the scene representation and fully leverage its explicit nature and speed advantage. Its explicit representation formulation allows us to devise a 2D prompt points to 3D mask dual-stage self-prompting segmentation algorithm, perform mask refinement and merging, minimize change as well as provide good initialization for scene inpainting and perform editing in real-time without per-editing training, all leads to superior quality and performance. We test our method by performing editing on both forward-facing and 360 scenes. We also compare our method against existing scene object removal methods, showing superior quality despite being more capable and having a speed advantage. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.16737.pdf)

<br>

## 3D Gaussian Rendering:
### 1. Mip-Splatting Alias-free 3D Gaussian Splatting 
**Authors**: Zehao Yu, Anpei Chen, Binbin Huang, Torsten Sattler, Andreas Geiger
<details span>
<summary><b>Abstract</b></summary>
Recently, 3D Gaussian Splatting (3DGS) has demonstrated impressive novel view synthesis results, reaching high fidelity and efficiency. However, strong artifacts can be observed when changing the sampling rate, e.g., by changing focal length or camera distance. We find that the source for this phenomenon can be attributed to the lack of 3D frequency constraints and the usage of a 2D dilation filter. To address this problem, we introduce a 3D smoothing filter which constrains the size of the 3D Gaussian primitives based on the maximal sampling frequency induced by the input views, eliminating high frequency artifacts when zooming in. Moreover, replacing 2D dilation with a 2D Mip filter, which simulates a 2D box filter, effectively mitigates aliasing and dilation issues. Our comprehensive evaluation, including scenarios such as training on single-scale images and testing on multiple scales, validates the effectiveness of our approach. 
</details>

  [📄 Paper](https://drive.google.com/file/d/1Q7KgGbynzcIEyFJV1I17HgrYz6xrOwRJ/view) | [🌐 Project Page](https://niujinshuchong.github.io/mip-splatting/) | [💻 Code](https://github.com/autonomousvision/mip-splatting) 

### 2. Relightable 3D Gaussian: Real-time Point Cloud Relighting with BRDF Decomposition and Ray Tracing 
**Authors**: Jian Gao, Chun Gu, Youtian Lin, Hao Zhu, Xun Cao, Li Zhang, Yao Yao 
<details span>
<summary><b>Abstract</b></summary>
We present a novel differentiable point-based rendering framework for material and lighting decomposition from multi-view images, enabling editing, ray-tracing, and real-time relighting of the 3D point cloud. Specifically, a 3D scene is represented as a set of relightable 3D Gaussian points, where each point is additionally associated with a normal direction, BRDF parameters, and incident lights from different directions. To achieve robust lighting estimation, we further divide incident lights of each point into global and local components, as well as view-dependent visibilities. The 3D scene is optimized through the 3D Gaussian Splatting technique while BRDF and lighting are decomposed by physically-based differentiable rendering. Moreover, we introduce an innovative point-based ray-tracing approach based on the bounding volume hierarchy for efficient visibility baking, enabling real-time rendering and relighting of 3D Gaussian points with accurate shadow effects. Extensive experiments demonstrate improved BRDF estimation and novel view rendering results compared to state-of-the-art material estimation approaches. Our framework showcases the potential to revolutionize the mesh-based graphics pipeline with a relightable, traceable, and editable rendering pipeline solely based on point cloud.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.16043.pdf) | [🌐 Project Page](https://nju-3dv.github.io/projects/Relightable3DGaussian/) | [💻 Code (not yet)]() 

### 3. GS-IR: 3D Gaussian Splatting for Inverse Rendering 
**Authors**: Zhihao Liang, Qi Zhang, Ying Feng, Ying Shan, Kui Jia 
<details span>
<summary><b>Abstract</b></summary>
We propose GS-IR, a novel inverse rendering approach based on 3D Gaussian Splatting (GS) that leverages forward mapping volume rendering to achieve photorealistic novel view synthesis and relighting results. Unlike previous works that use implicit neural representations and volume rendering (e.g. NeRF), which suffer from low expressive power and high computational complexity, we extend GS, a top-performance representation for novel view synthesis, to estimate scene geometry, surface material, and environment illumination from multi-view images captured under unknown lighting conditions. There are two main problems when introducing GS to inverse rendering: 1) GS does not support producing plausible normal natively; 2) forward mapping (e.g. rasterization and splatting) cannot trace the occlusion like backward mapping (e.g. ray tracing). To address these challenges, our GS-IR proposes an efficient optimization scheme that incorporates a depth-derivation-based regularization for normal estimation and a baking-based occlusion to model indirect lighting. The flexible and expressive GS representation allows us to achieve fast and compact geometry reconstruction, photorealistic novel view synthesis, and effective physically-based rendering. We demonstrate the superiority of our method over baseline methods through qualitative and quantitative evaluations on various challenging scenes. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.16473.pdf) | [🌐 Project Page](https://github.com/lzhnb/GS-IR) | [💻 Code (not yet)](https://github.com/lzhnb/GS-IR) 

### 4. Multi-Scale 3D Gaussian Splatting for Anti-Aliased Rendering  
**Authors**: Zhiwen Yan, Weng Fei Low, Yu Chen, Gim Hee Lee 
<details span>
<summary><b>Abstract</b></summary>
3D Gaussians have recently emerged as a highly efficient representation for 3D reconstruction and rendering. Despite its high rendering quality and speed at high resolutions, they both deteriorate drastically when rendered at lower resolutions or from far away camera position. During low resolution or far away rendering, the pixel size of the image can fall below the Nyquist frequency compared to the screen size of each splatted 3D Gaussian and leads to aliasing effect. The rendering is also drastically slowed down by the sequential alpha blending of more splatted Gaussians per pixel. To address these issues, we propose a multi-scale 3D Gaussian splatting algorithm, which maintains Gaussians at different scales to represent the same scene. Higher-resolution images are rendered with more small Gaussians, and lower-resolution images are rendered with fewer larger Gaussians. With similar training time, our algorithm can achieve 13\%-66\% PSNR and 160\%-2400\% rendering speed improvement at 4×-128× scale rendering on Mip-NeRF360 dataset compared to the single scale 3D Gaussian splatting. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.17089.pdf) 

### 5. GaussianShader: 3D Gaussian Splatting with Shading Functions for Reflective Surfaces 
**Authors**: Yingwenqi Jiang, Jiadong Tu, Yuan Liu, Xifeng Gao, Xiaoxiao Long, Wenping Wang, Yuexin Ma 
<details span>
<summary><b>Abstract</b></summary>
The advent of neural 3D Gaussians has recently brought about a revolution in the field of neural rendering, facilitating the generation of high-quality renderings at real-time speeds. However, the explicit and discrete representation encounters challenges when applied to scenes featuring reflective surfaces. In this paper, we present GaussianShader, a novel method that applies a simplified shading function on 3D Gaussians to enhance the neural rendering in scenes with reflective surfaces while preserving the training and rendering efficiency. The main challenge in applying the shading function lies in the accurate normal estimation on discrete 3D Gaussians. Specifically, we proposed a novel normal estimation framework based on the shortest axis directions of 3D Gaussians with a delicately designed loss to make the consistency between the normals and the geometries of Gaussian spheres. Experiments show that GaussianShader strikes a commendable balance between efficiency and visual quality. Our method surpasses Gaussian Splatting in PSNR on specular object datasets, exhibiting an improvement of 1.57dB. When compared to prior works handling reflective surfaces, such as Ref-NeRF, our optimization time is significantly accelerated (23h vs. 0.58h). Please click on our project website to see more results. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.17977.pdf) | [🌐 Project Page](https://asparagus15.github.io/GaussianShader.github.io/) | [💻 Code](https://github.com/Asparagus15/GaussianShader) 

<br>

## 3D Gaussian Compression:
### 1. LightGaussian: Unbounded 3D Gaussian Compression with 15x Reduction and 200+ FPS 
**Authors**: Zhiwen Fan, Kevin Wang, Kairun Wen, Zehao Zhu, Dejia Xu, Zhangyang Wang 
<details span>
<summary><b>Abstract</b></summary>
Recent advancements in real-time neural rendering using point-based techniques have paved the way for the widespread adoption of 3D representations. However, foundational approaches like 3D Gaussian Splatting come with a substantial storage overhead caused by growing the SfM points to millions, often demanding gigabyte-level disk space for a single unbounded scene, posing significant scalability challenges and hindering the splatting efficiency.
To address this challenge, we introduce LightGaussian, a novel method designed to transform 3D Gaussians into a more efficient and compact format. Drawing inspiration from the concept of Network Pruning, LightGaussian identifies Gaussians that are insignificant in contributing to the scene reconstruction and adopts a pruning and recovery process, effectively reducing redundancy in Gaussian counts while preserving visual effects. Additionally, LightGaussian employs distillation and pseudo-view augmentation to distill spherical harmonics to a lower degree, allowing knowledge transfer to more compact representations while maintaining reflectance. Furthermore, we propose a hybrid scheme, VecTree Quantization, to quantize all attributes, resulting in lower bitwidth representations with minimal accuracy losses.
In summary, LightGaussian achieves an averaged compression rate over 15x while boosting the FPS from 139 to 215, enabling an efficient representation of complex scenes on Mip-NeRF 360, Tank and Temple datasets. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.17245.pdf) | [🌐 Project Page](https://lightgaussian.github.io/) | [💻 Code](https://github.com/VITA-Group/LightGaussian) | [🎥 Short Presentation](https://youtu.be/470hul75bSM?si=EKm-UaBaTs9qJH6K)

### 2. Compact3D: Compressing Gaussian Splat Radiance Field Models with Vector Quantization 
**Authors**: KL Navaneet, Kossar Pourahmadi Meibodi, Soroush Abbasi Koohpayegani, Hamed Pirsiavash 
<details span>
<summary><b>Abstract</b></summary>
3D Gaussian Splatting is a new method for modeling and rendering 3D radiance fields that achieves much faster learning and rendering time compared to SOTA NeRF methods. However, it comes with a drawback in the much larger storage demand compared to NeRF methods since it needs to store the parameters for several 3D Gaussians. We notice that many Gaussians may share similar parameters, so we introduce a simple vector quantization method based on \kmeans algorithm to quantize the Gaussian parameters. Then, we store the small codebook along with the index of the code for each Gaussian. Moreover, we compress the indices further by sorting them and using a method similar to run-length encoding. We do extensive experiments on standard benchmarks as well as a new benchmark which is an order of magnitude larger than the standard benchmarks. We show that our simple yet effective method can reduce the storage cost for the original 3D Gaussian Splatting method by a factor of almost 20× with a very small drop in the quality of rendered images. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.18159.pdf) | [💻 Code](https://github.com/UCDvision/compact3d)

<br>

## Misc:
### 1. FisherRF: Active View Selection and Uncertainty Quantification for Radiance Fields using Fisher Information  
**Authors**: Wen Jiang, Boshu Lei, Kostas Daniilidis 
<details span>
<summary><b>Abstract</b></summary>
This study addresses the challenging problem of active view selection and uncertainty quantification within the domain of Radiance Fields. Neural Radiance Fields (NeRF) have greatly advanced image rendering and reconstruction, but the limited availability of 2D images poses uncertainties stemming from occlusions, depth ambiguities, and imaging errors. Efficiently selecting informative views becomes crucial, and quantifying NeRF model uncertainty presents intricate challenges. Existing approaches either depend on model architecture or are based on assumptions regarding density distributions that are not generally applicable. By leveraging Fisher Information, we efficiently quantify observed information within Radiance Fields without ground truth data. This can be used for the next best view selection and pixel-wise uncertainty quantification. Our method overcomes existing limitations on model architecture and effectiveness, achieving state-of-the-art results in both view selection and uncertainty quantification, demonstrating its potential to advance the field of Radiance Fields. Our method with the 3D Gaussian Splatting backend could perform view selections at 70 fps. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.17874.pdf) | [🌐 Project Page](https://jiangwenpl.github.io/FisherRF/) | [💻 Code (not yet)](https://github.com/JiangWenPL/FisherRF) 

### 2. Periodic Vibration Gaussian: Dynamic Urban Scene Reconstruction and Real-time Rendering 
**Authors**: Yurui Chen, Chun Gu, Junzhe Jiang, Xiatian Zhu, Li Zhang 
<details span>
<summary><b>Abstract</b></summary>
Modeling dynamic, large-scale urban scenes is challenging due to their highly intricate geometric structures and unconstrained dynamics in both space and time. Prior methods often employ high-level architectural priors, separating static and dynamic elements, resulting in suboptimal capture of their synergistic interactions. To address this challenge, we present a unified representation model, called Periodic Vibration Gaussian (PVG). PVG builds upon the efficient 3D Gaussian splatting technique, originally designed for static scene representation, by introducing periodic vibration-based temporal dynamics. This innovation enables PVG to elegantly and uniformly represent the characteristics of various objects and elements in dynamic urban scenes. To enhance temporally coherent representation learning with sparse training data, we introduce a novel flow-based temporal smoothing mechanism and a position-aware adaptive control strategy. Extensive experiments on Waymo Open Dataset and KITTI benchmarks demonstrate that PVG surpasses state-of-the-art alternatives in both reconstruction and novel view synthesis for both dynamic and static scenes. Notably, PVG achieves this without relying on manually labeled object bounding boxes or expensive optical flow estimation. Moreover, PVG exhibits 50/6000-fold acceleration in training/rendering over the best alternative. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.18561.pdf) | [🌐 Project Page](https://fudan-zvg.github.io/PVG/) | [💻 Code (not yet)](https://github.com/fudan-zvg/PVG) 

<br>

## Classic work:
### 1. A Generalization of Algebraic Surface Drawing
**Authors**: James F. Blinn

 ***Comment:***: First paper rendering 3D gaussians.

<details span>
<summary><b>Abstract</b></summary>
The mathematical description of three-dimensional surfaces usually falls into one of two classifications: 
parametric and implicit. An implicit surface is defined to be all points which satisfy some
equation F (x, y, z) = 0. This form is ideally suited for image space shaded picture drawing; the pixel
coordinates are substituted for x and y, and the equation is solved for z. Algorithms for drawing such
objects have been developed primarily for fLrst- and second-order polynomial functions, a subcategory
known as algebraic surfaces. This paper presents a new algorithm applicable to other functional
forms, in particular to the summation of several Gaussian density distributions. The algorithm was
created to model electron density maps of molecular structures, but it can be used for other artistically
interesting shapes.
</details>

[📄 Paper](https://dl.acm.org/doi/pdf/10.1145/357306.357310) 

### 2. Approximate Differentiable Rendering with Algebraic Surfaces
**Authors**: Leonid Keselman and Martial Hebert

 ***Comment:***: First paper to do differentiable rendering optimization of 3D gaussians.

<details span>
<summary><b>Abstract</b></summary>
Differentiable renderers provide a direct mathematical link
between an object’s 3D representation and images of that object. In
this work, we develop an approximate differentiable renderer for a compact, interpretable representation, which we call Fuzzy Metaballs. Our
approximate renderer focuses on rendering shapes via depth maps and
silhouettes. It sacrifices fidelity for utility, producing fast runtimes and
high-quality gradient information that can be used to solve vision tasks.
Compared to mesh-based differentiable renderers, our method has forward passes that are 5x faster and backwards passes that are 30x faster.
The depth maps and silhouette images generated by our method are
smooth and defined everywhere. In our evaluation of differentiable renderers for pose estimation, we show that our method is the only one
comparable to classic techniques. In shape from silhouette, our method
performs well using only gradient descent and a per-pixel loss, without
any surrogate losses or regularization. These reconstructions work well
even on natural video sequences with segmentation artifacts.
</details>

[📄 Paper](https://arxiv.org/pdf/2309.16585.pdf) | [🌐 Project Page](https://leonidk.com/fuzzy-metaballs/) | [💻 Code](https://github.com/leonidk/fuzzy-metaballs) | [🎥 Short Presentation](https://www.youtube.com/watch?v=Ec7cxEc9eOU) 

### 3. Unbiased Gradient Estimation for Differentiable Surface Splatting via Poisson Sampling
**Authors**: Jan U. Müller, Michael Weinmann, Reinhard Klein

***Comment:*** Builds 2D screen-space gaussians from underlying 3D representations.

<details span>
<summary><b>Abstract</b></summary>
The mathematical description of three-dimensional surfaces usually falls into one of two classifica-
tions: parametric and implicit. An implicit surface is defined to be all points which satisfy some
equation F (x, y, z) = 0. This form is ideally suited for image space shaded picture drawing; the pixel
coordinates are substituted for x and y, and the equation is solved for z. Algorithms for drawing such
objects have been developed primarily for fLrst- and second-order polynomial functions, a subcategory
known as algebraic surfaces. This paper presents a new algorithm applicable to other functional
forms, in particular to the summation of several Gaussian density distributions. The algorithm was
created to model electron density maps of molecular structures, but it can be used for other artistically
interesting shapes.
</details>

[📄 Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136930276.pdf) [💻 Code](https://github.com/muellerju/unbiased-differentiable-splatting) 

### 4. Generating and Real-Time Rendering of Clouds
**Authors**: Petr Man

***Comment:*** Splatting of anisotropic gaussians. Basically a non-differentiable implementation of 3DGS.

<details span>
<summary><b>Abstract</b></summary>
This paper presents a method for generation and real-time
rendering of static clouds. Perlin noise function generates
three dimensional map of a cloud. We also present a twopass rendering algorithm that performs physically based
approximation. In the first preprocessed phase it computes
multiple forward scattering. In the second phase first order
anisotropic scattering at runtime is evaluated.
The generated map is stored as voxels and is unsuitable
for the real-time rendering. We introduce a more suitable
inner representation of cloud that approximates the original map and contains much less information. The cloud is
then represented by a set of metaballs (spheres) with parameters such as center positions, radii and density values.
The main contribution of this paper is to propose a
method, that transforms the original cloud map to the inner
representation. This method uses the Radial Basis Function (RBF) neural network.
</details>

[📄 Paper](https://old.cescg.org/CESCG-2006/papers/Prague-Man-Petr.pdf) 

<br>

## Open Source Implementations 

### Reference 
- [Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting)

### Unofficial Implementations
- [Taichi 3D Gaussian Splatting](https://github.com/wanmeihuali/taichi_3d_gaussian_splatting)
- [Gaussian Splatting 3D](https://github.com/heheyas/gaussian_splatting_3d)
- [3D Gaussian Splatting](https://github.com/WangFeng18/3d-gaussian-splatting)
- [fast: C++/CUDA](https://github.com/MrNeRF/gaussian-splatting-cuda)
- [nerfstudio: python/CUDA](https://github.com/nerfstudio-project/gsplat)

### 2D Gaussian Splatting
- [jupyter notebook 2D GS splatting](https://github.com/OutofAi/2D-Gaussian-Splatting)

### Game Engines 
- [Unity](https://github.com/aras-p/UnityGaussianSplatting)
- [PlayCanvas](https://github.com/playcanvas/engine/tree/main/extras/splat)
- [Unreal](https://github.com/xverse-engine/XV3DGS-UEPlugin)

### Viewers
- [WebGL Viewer 1](https://github.com/antimatter15/splat)
- [WebGL Viewer 2](https://github.com/kishimisu/Gaussian-Splatting-WebGL)
- [WebGPU Viewer 1](https://github.com/cvlab-epfl/gaussian-splatting-web)
- [WebGPU Viewer 2](https://github.com/MarcusAndreasSvensson/gaussian-splatting-webgpu)
- [Three.js](https://github.com/mkkellogg/GaussianSplats3D)
- [A-Frame](https://github.com/quadjr/aframe-gaussian-splatting)
- [Nerfstudio Unofficial](https://github.com/yzslab/nerfstudio/tree/gaussian_splatting)
- [Nerfstudio Viser](https://github.com/nerfstudio-project/viser)
- [Blender (Editor)](https://github.com/ReshotAI/gaussian-splatting-blender-addon/tree/master)
- [WebRTC viewer](https://github.com/dylanebert/gaussian-viewer)
- [iOS & Metal viewer](https://github.com/laanlabs/metal-splats)
- [jupyter notebook](https://github.com/shumash/gaussian-splatting/blob/mshugrina/interactive/interactive.ipynb)
- [python OpenGL viewer](https://github.com/limacv/GaussianSplattingViewer.git)
- [PlayCanvas Viewer](https://github.com/playcanvas/model-viewer)
- [gsplat.js](https://github.com/dylanebert/gsplat.js)

### Utilities
- [Kapture](https://github.com/naver/kapture) - a unified data format to facilitate visual localization and structure from motion e.g. for bundler to colmap model conversion
- [Kapture image cropper script](https://gist.github.com/jo-chemla/258e6e40d3d6c2220b29518ff3c17c40) - undistorted image cropper script to remove black borders with included conversion instructions
- [camorph](https://github.com/Fraunhofer-IIS/camorph) - a toolbox for conversion between camera parameter conventions e.g. Reality Capture to colmap model
- [3DGS Converter](https://github.com/francescofugazzi/3dgsconverter) - a tool for converting 3D Gaussian Splatting .ply files into a format suitable for Cloud Compare and vice-versa.
- [SuperSplat](https://github.com/playcanvas/super-splat) - open source browser-based tool to clean up and reorient .ply files

## Blog Posts

1. [Gaussian Splatting is pretty cool](https://aras-p.info/blog/2023/09/05/Gaussian-Splatting-is-pretty-cool/)
2. [Making Gaussian Splats smaller](https://aras-p.info/blog/2023/09/13/Making-Gaussian-Splats-smaller/)
3. [Making Gaussian Splats more smaller](https://aras-p.info/blog/2023/09/27/Making-Gaussian-Splats-more-smaller/)
4. [Introduction to 3D Gaussian Splatting](https://huggingface.co/blog/gaussian-splatting)
5. [Very good (technical) intro to 3D Gaussian Splatting](https://medium.com/@AriaLeeNotAriel/numbynum-3d-gaussian-splatting-for-real-time-radiance-field-rendering-kerbl-et-al-60c0b25e5544)
6. [Write up on some mathematical details of the 3DGS implementation](https://github.com/kwea123/gaussian_splatting_notes)
7. [Discussion about gs universal format](https://github.com/mkkellogg/GaussianSplats3D/issues/47#issuecomment-1801360116)
8. [Math explanation to understand 3DGS](https://github.com/chiehwangs/3d-gaussian-theory)

## Tutorial Videos

1. [Getting Started with 3DGS for Windows](https://youtu.be/UXtuigy_wYc?si=j1vfORNspcocSH-b)
2. [How to view 3DGS Scenes in Unity](https://youtu.be/5_GaPYBHqOo?si=6u9j1HqXwF_5WSUL)
3. [Two-minute explanation of 3DGS](https://youtu.be/HVv_IQKlafQ?si=w5c9XKHfKIBuXDLW)
4. [Jupyter notebook tutorial](https://www.youtube.com/watch?v=OcvA7fmiZYM&t=2s)
5. [Intro to gaussian splatting (and Unity plugin)](https://www.xuanprada.com/blog/2023/10/22/intro-to-gaussian-splatting)

## Credits

- Thanks to [Leonid Keselman](https://github.com/leonidk) for informing me about the release of the paper "Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting".
- Thanks to [Eric Haines](https://github.com/erich666) for suggesting the jupyter notebook viewer, windows tutorial and for fixing text hyphenations and other issues.
- Thanks to [Henry Pearce](https://github.com/henrypearce4D) for maintaining contributions.
