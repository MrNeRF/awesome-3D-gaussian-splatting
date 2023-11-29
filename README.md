# Awesome 3D Gaussian Splatting Resources 

A curated list of papers and open-source resources focused on 3D Gaussian Splatting, intended to keep pace with the anticipated surge of research in the coming months. If you have any additions or suggestions, feel free to contribute. Additional resources like blog posts, videos, etc. are also welcome.

<details span>
<summary><b>Update Log:</b></summary>
<br>

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
  - Some notes about the 3DGS implementation and unsiversal format discussion.

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

## Seminal Paper introducing 3D Gaussian Splatting:
### 3D Gaussian Splatting for Real-Time Radiance Field Rendering
**Authors**: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis

<details open>
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

## Dynamic 3D Gaussian Splatting:
### 1. Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis
**Authors**: Jonathon Luiten, Georgios Kopanas, Bastian Leibe, Deva Ramanan

<details open>
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

<details open>
<summary><b>Abstract</b></summary>
Implicit neural representation has opened up new avenues for dynamic scene reconstruction and rendering. Nonetheless, state-of-the-art methods of dynamic neural rendering rely heavily on these implicit representations, which frequently struggle with accurately capturing the intricate details of objects in the scene. Furthermore, implicit methods struggle to achieve real-time rendering in general dynamic scenes, limiting their use in a wide range of tasks. To address the issues, we propose a deformable 3D Gaussians Splatting method that reconstructs scenes using explicit 3D Gaussians and learns Gaussians in canonical space with a deformation field to model monocular dynamic scenes. We also introduced a smoothing training mechanism with no extra overhead to mitigate the impact of inaccurate poses in real datasets on the smoothness of time interpolation tasks. Through differential gaussian rasterization, the deformable 3D Gaussians not only achieve higher rendering quality but also real-time rendering speed. Experiments show that our method outperforms existing methods significantly in terms of both rendering quality and speed, making it well-suited for tasks such as novel-view synthesis, time synthesis, and real-time rendering. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2309.13101.pdf) | [🌐 Project Page](https://ingra14m.github.io/Deformable-Gaussians/) | [💻 Code](https://github.com/ingra14m/Deformable-3D-Gaussians) 

### 3. 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering
**Authors**: Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Tian Qi, Xinggang Wang

<details open>
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

<details open>
<summary><b>Abstract</b></summary>
Reconstructing dynamic 3D scenes from 2D images and generating diverse views over time is challenging due to scene complexity and temporal dynamics. Despite advancements in neural implicit models, limitations persist: (i) Inadequate Scene Structure: Existing methods struggle to reveal the spatial and temporal structure of dynamic scenes from directly learning the complex 6D plenoptic function. (ii) Scaling Deformation Modeling: Explicitly modeling scene element deformation becomes impractical for complex dynamics. To address these issues, we consider the spacetime as an entirety and propose to approximate the underlying spatio-temporal 4D volume of a dynamic scene by optimizing a collection of 4D primitives, with explicit geometry and appearance modeling. Learning to optimize the 4D primitives enables us to synthesize novel views at any desired time with our tailored rendering routine. Our model is conceptually simple, consisting of a 4D Gaussian parameterized by anisotropic ellipses that can rotate arbitrarily in space and time, as well as view-dependent and time-evolved appearance represented by the coefficient of 4D spherindrical harmonics. This approach offers simplicity, flexibility for variable-length video and end-to-end training, and efficient real-time rendering, making it suitable for capturing complex dynamic scene motions. Experiments across various benchmarks, including monocular and multi-view scenarios, demonstrate our 4DGS model's superior visual quality and efficiency. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2310.10642.pdf) | [💻 Code (to be released)](https://github.com/fudan-zvg/4d-gaussian-splatting) 

### 5. An Efficient 3D Gaussian Representation for Monocular/Multi-view Dynamic Scenes 
**Authors**: Kai Katsumata, Duc Minh Vo, Hideki Nakayama 

<details open>
<summary><b>Abstract</b></summary>
In novel view synthesis of scenes from multiple input views, 3D Gaussian splatting emerges as a viable alternative to existing radiance field approaches, delivering great visual quality and real-time rendering. While successful in static scenes, the present advancement of 3D Gaussian representation, however, faces challenges in dynamic scenes in terms of memory consumption and the need for numerous observations per time step, due to the onus of storing 3D Gaussian parameters per time step. In this study, we present an efficient 3D Gaussian representation tailored for dynamic scenes in which we define positions and rotations as functions of time while leaving other time-invariant properties of the static 3D Gaussian unchanged. Notably, our representation reduces memory usage, which is consistent regardless of the input sequence length. Additionally, it mitigates the risk of overfitting observed frames by accounting for temporal changes. The optimization of our Gaussian representation based on image and flow reconstruction results in a powerful framework for dynamic scene view synthesis in both monocular and multi-view cases. We obtain the highest rendering speed of 118 frames per second (FPS) at a resolution of 1352×1014 with a single GPU, showing the practical usability and effectiveness of our proposed method in dynamic scene rendering scenarios
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.12897.pdf) 

## Diffusion 3D Gaussian Splatting:

### 1. Text-to-3D using Gaussian Splatting
**Authors**: Zilong Chen, Feng Wang, Huaping Liu

<details open>
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

<details open>
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
<details open>
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
<details open>
<summary><b>Abstract</b></summary>
 Text-to-3D, known for its efficient generation methods and expansive creative potential, has garnered significant attention in the AIGC domain. However, the amalgamation of Nerf and 2D diffusion models frequently yields oversaturated images, posing severe limitations on downstream industrial applications due to the constraints of pixelwise rendering method. Gaussian splatting has recently superseded the traditional pointwise sampling technique prevalent in NeRF-based methodologies, revolutionizing various aspects of 3D reconstruction. This paper introduces a novel text to 3D content generation framework based on Gaussian splatting, enabling fine control over image saturation through individual Gaussian sphere transparencies, thereby producing more realistic images. The challenge of achieving multi-view consistency in 3D generation significantly impedes modeling complexity and accuracy. Taking inspiration from SJC, we explore employing multi-view noise distributions to perturb images generated by 3D Gaussian splatting, aiming to rectify inconsistencies in multi-view geometry. We ingeniously devise an efficient method to generate noise that produces Gaussian noise from diverse viewpoints, all originating from a shared noise source. Furthermore, vanilla 3D Gaussian-based generation tends to trap models in local minima, causing artifacts like floaters, burrs, or proliferative elements. To mitigate these issues, we propose the variational Gaussian splatting technique to enhance the quality and stability of 3D appearance. To our knowledge, our approach represents the first comprehensive utilization of Gaussian splatting across the entire spectrum of 3D content generation processes.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.11221.pdf)  

### 5. LucidDreamer: Towards High-Fidelity Text-to-3D Generation via Interval Score Matching  
Yixun Liang, Xin Yang, Jiantao Lin, Haodong Li, Xiaogang Xu, Yingcong Chen
<details open>
<summary><b>Abstract</b></summary>
The recent advancements in text-to-3D generation mark a significant milestone in generative models, unlocking new possibilities for creating imaginative 3D assets across various real-world scenarios. While recent advancements in text-to-3D generation have shown promise, they often fall short in rendering detailed and high-quality 3D models. This problem is especially prevalent as many methods base themselves on Score Distillation Sampling (SDS). This paper identifies a notable deficiency in SDS, that it brings inconsistent and low-quality updating direction for the 3D model, causing the over-smoothing effect. To address this, we propose a novel approach called Interval Score Matching (ISM). ISM employs deterministic diffusing trajectories and utilizes interval-based score matching to counteract over-smoothing. Furthermore, we incorporate 3D Gaussian Splatting into our text-to-3D generation pipeline. Extensive experiments show that our model largely outperforms the state-of-the-art in quality and training efficiency.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.11284.pdf) | [💻 Code](https://github.com/EnVision-Research/LucidDreamer) 

### 6. LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes
Jaeyoung Chung, Suyoung Lee, Hyeongjin Nam, Jaerin Lee, Kyoung Mu Lee
<details open>
<summary><b>Abstract</b></summary>
With the widespread usage of VR devices and contents, demands for 3D scene generation techniques become more popular. Existing 3D scene generation models, however, limit the target scene to specific domain, primarily due to their training strategies using 3D scan dataset that is far from the real-world. To address such limitation, we propose LucidDreamer, a domain-free scene generation pipeline by fully leveraging the power of existing large-scale diffusion-based generative model. Our LucidDreamer has two alternate steps: Dreaming and Alignment. First, to generate multi-view consistent images from inputs, we set the point cloud as a geometrical guideline for each image generation. Specifically, we project a portion of point cloud to the desired view and provide the projection as a guidance for inpainting using the generative model. The inpainted images are lifted to 3D space with estimated depth maps, composing a new points. Second, to aggregate the new points into the 3D scene, we propose an aligning algorithm which harmoniously integrates the portions of newly generated 3D scenes. The finally obtained 3D scene serves as initial points for optimizing Gaussian splats. LucidDreamer produces Gaussian splats that are highly-detailed compared to the previous 3D scene generation methods, with no constraint on domain of the target scene. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.13384.pdf) | [🌐 Project Page](https://luciddreamer-cvlab.github.io/) | [💻 Code (not yet)](https://github.com/anonymous-luciddreamer/LucidDreamer) 

### 7. HumanGaussian: Text-Driven 3D Human Generation with Gaussian Splatting  
Xian Liu, Xiaohang Zhan, Jiaxiang Tang, Ying Shan, Gang Zeng, Dahua Lin, Xihui Liu, Ziwei Liu
<details open>
<summary><b>Abstract</b></summary>
Realistic 3D human generation from text prompts is a desirable yet challenging task. Existing methods optimize 3D representations like mesh or neural fields via score distillation sampling (SDS), which suffers from inadequate fine details or excessive training time. In this paper, we propose an efficient yet effective framework, HumanGaussian, that generates high-quality 3D humans with fine-grained geometry and realistic appearance. Our key insight is that 3D Gaussian Splatting is an efficient renderer with periodic Gaussian shrinkage or growing, where such adaptive density control can be naturally guided by intrinsic human structures. Specifically, 1) we first propose a Structure-Aware SDS that simultaneously optimizes human appearance and geometry. The multi-modal score function from both RGB and depth space is leveraged to distill the Gaussian densification and pruning process. 2) Moreover, we devise an Annealed Negative Prompt Guidance by decomposing SDS into a noisier generative score and a cleaner classifier score, which well addresses the over-saturation issue. The floating artifacts are further eliminated based on Gaussian size in a prune-only phase to enhance generation smoothness. Extensive experiments demonstrate the superior efficiency and competitive quality of our framework, rendering vivid 3D humans under diverse scenarios.
</details>

  [📄 Paper](https://alvinliu0.github.io/projects/HumanGaussian/humangaussian.pdf) | [🌐 Project Page](https://alvinliu0.github.io/projects/HumanGaussian) | [💻 Code](https://github.com/alvinliu0/HumanGaussian) | [🎥 Short Presentation](https://www.youtube.com/watch?v=S3djzHoqPKY)

## 3D Gaussian Splatting Avatars:
### 1. Drivable 3D Gaussian Avatars 
**Authors**:  Wojciech Zielonka, Timur Bagautdinov, Shunsuke Saito, Michael Zollhöfer, Justus Thies, Javier Romero
<details open>
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
<details open>
<summary><b>Abstract</b></summary>
We propose SplatArmor, a novel approach for recovering detailed and animatable human models by `armoring' a parameterized body model with 3D Gaussians. Our approach represents the human as a set of 3D Gaussians within a canonical space, whose articulation is defined by extending the skinning of the underlying SMPL geometry to arbitrary locations in the canonical space. To account for pose-dependent effects, we introduce a SE(3) field, which allows us to capture both the location and anisotropy of the Gaussians. Furthermore, we propose the use of a neural color field to provide color regularization and 3D supervision for the precise positioning of these Gaussians. We show that Gaussian splatting provides an interesting alternative to neural rendering based methods by leverging a rasterization primitive without facing any of the non-differentiability and optimization challenges typically faced in such approaches. The rasterization paradigms allows us to leverage forward skinning, and does not suffer from the ambiguities associated with inverse skinning and warping. We show compelling results on the ZJU MoCap and People Snapshot datasets, which underscore the effectiveness of our method for controllable human synthesis.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.10812.pdf) 

### 3. Animatable 3D Gaussians for High-fidelity Synthesis of Human Motions 
**Authors**: Keyang Ye, Tianjia Shao, Kun Zhou 
<details open>
<summary><b>Abstract</b></summary>
We present a novel animatable 3D Gaussian model for rendering high-fidelity free-view human motions in real time. Compared to existing NeRF-based methods, the model owns better capability in synthesizing high-frequency details without the jittering problem across video frames. The core of our model is a novel augmented 3D Gaussian representation, which attaches each Gaussian with a learnable code. The learnable code serves as a pose-dependent appearance embedding for refining the erroneous appearance caused by geometric transformation of Gaussians, based on which an appearance refinement model is learned to produce residual Gaussian properties to match the appearance in target pose. To force the Gaussians to learn the foreground human only without background interference, we further design a novel alpha loss to explicitly constrain the Gaussians within the human body. We also propose to jointly optimize the human joint parameters to improve the appearance accuracy. The animatable 3D Gaussian model can be learned with shallow MLPs, so new human motions can be synthesized in real time (66 fps on avarage). Experiments show that our model has superior performance over NeRF-based methods. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.13404.pdf) 
  
### 4. Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling 
**Authors**: Zhe Li, Zerong Zheng, Lizhen Wang, Yebin Liu 
<details open>
<summary><b>Abstract</b></summary>
Modeling animatable human avatars from RGB videos is a long-standing and challenging problem. Recent works usually adopt MLP-based neural radiance fields (NeRF) to represent 3D humans, but it remains difficult for pure MLPs to regress pose-dependent garment details. To this end, we introduce Animatable Gaussians, a new avatar representation that leverages powerful 2D CNNs and 3D Gaussian splatting to create high-fidelity avatars. To associate 3D Gaussians with the animatable avatar, we learn a parametric template from the input videos, and then parameterize the template on two front & back canonical Gaussian maps where each pixel represents a 3D Gaussian. The learned template is adaptive to the wearing garments for modeling looser clothes like dresses. Such template-guided 2D parameterization enables us to employ a powerful StyleGAN-based CNN to learn the pose-dependent Gaussian maps for modeling detailed dynamic appearances. Furthermore, we introduce a pose projection strategy for better generalization given novel poses. Overall, our method can create lifelike avatars with dynamic, realistic and generalized appearances. Experiments show that our method outperforms other state-of-the-art approaches. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.16096.pdf) | [🌐 Project Page](https://animatable-gaussians.github.io/) | [💻 Code (not yet)](https://github.com/lizhe00/AnimatableGaussians)

### 5. GART: Gaussian Articulated Template Models 
**Authors**: Jiahui Lei, Yufu Wang, Georgios Pavlakos, Lingjie Liu, Kostas Daniilidis 
<details open>
<summary><b>Abstract</b></summary>
We introduce Gaussian Articulated Template Model GART, an explicit, efficient, and expressive representation for non-rigid articulated subject capturing and rendering from monocular videos. GART utilizes a mixture of moving 3D Gaussians to explicitly approximate a deformable subject's geometry and appearance. It takes advantage of a categorical template model prior (SMPL, SMAL, etc.) with learnable forward skinning while further generalizing to more complex non-rigid deformations with novel latent bones. GART can be reconstructed via differentiable rendering from monocular videos in seconds or minutes and rendered in novel poses faster than 150fps.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.16099.pdf) | [🌐 Project Page](https://www.cis.upenn.edu/~leijh/projects/gart/) | [💻 Code](https://github.com/JiahuiLei/GART)


## 3D Gaussian Splatting SLAM:
### 1. GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting 
**Authors**: Chi Yan, Delin Qu, Dong Wang, Dan Xu, Zhigang Wang, Bin Zhao, Xuelong Li
<details open>
<summary><b>Abstract</b></summary>
In this paper, we introduce GS-SLAM that first utilizes 3D Gaussian representation in the Simultaneous Localization and Mapping (SLAM) system. It facilitates a better balance between efficiency and accuracy. Compared to recent SLAM methods employing neural implicit representations, our method utilizes a real-time differentiable splatting rendering pipeline that offers significant speedup to map optimization and RGB-D re-rendering. Specifically, we propose an adaptive expansion strategy that adds new or deletes noisy 3D Gaussian in order to efficiently reconstruct new observed scene geometry and improve the mapping of previously observed areas. This strategy is essential to extend 3D Gaussian representation to reconstruct the whole scene rather than synthesize a static object in existing methods. Moreover, in the pose tracking process, an effective coarse-to-fine technique is designed to select reliable 3D Gaussian representations to optimize camera pose, resulting in runtime reduction and robust estimation. Our method achieves competitive performance compared with existing state-of-the-art real-time methods on the Replica, TUM-RGBD datasets. The source code will be released upon acceptance. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.11700.pdf) 

## 3D Gaussian Splatting Mesh Extraction and Physics:
### 1. PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics
**Authors**: Tianyi Xie, Zeshun Zong, Yuxin Qiu, Xuan Li, Yutao Feng, Yin Yang, Chenfanfu Jiang
<details open>
<summary><b>Abstract</b></summary>
We introduce PhysGaussian, a new method that seamlessly integrates physically grounded Newtonian dynamics within 3D Gaussians to achieve high-quality novel motion synthesis. Employing a custom Material Point Method (MPM), our approach enriches 3D Gaussian kernels with physically meaningful kinematic deformation and mechanical stress attributes, all evolved in line with continuum mechanics principles. A defining characteristic of our method is the seamless integration between physical simulation and visual rendering: both components utilize the same 3D Gaussian kernels as their discrete representations. This negates the necessity for triangle/tetrahedron meshing, marching cubes, "cage meshes," or any other geometry embedding, highlighting the principle of "what you see is what you simulate (WS2)." Our method demonstrates exceptional versatility across a wide variety of materials--including elastic entities, metals, non-Newtonian fluids, and granular materials--showcasing its strong capabilities in creating diverse visual content with novel viewpoints and movements. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.12198.pdf) | [🌐 Project Page](https://xpandora.github.io/PhysGaussian/) | [💻 Code (not released yet)](https://github.com/XPandora/PhysGaussian) | [🎥 Short Presentation](https://drive.google.com/file/d/1eh7vxRxer7gfvPhs8jDE56oRjayBc9oe/view)

### 2. SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering 
**Authors**: Antoine Guédon, Vincent Lepetit
<details open>
<summary><b>Abstract</b></summary>
We propose a method to allow precise and extremely fast mesh extraction from 3D Gaussian Splatting. Gaussian Splatting has recently become very popular as it yields realistic rendering while being significantly faster to train than NeRFs. It is however challenging to extract a mesh from the millions of tiny 3D gaussians as these gaussians tend to be unorganized after optimization and no method has been proposed so far. Our first key contribution is a regularization term that encourages the gaussians to align well with the surface of the scene. We then introduce a method that exploits this alignment to sample points on the real surface of the scene and extract a mesh from the Gaussians using Poisson reconstruction, which is fast, scalable, and preserves details, in contrast to the Marching Cubes algorithm usually applied to extract meshes from Neural SDFs. Finally, we introduce an optional refinement strategy that binds gaussians to the surface of the mesh, and jointly optimizes these Gaussians and the mesh through Gaussian splatting rendering. This enables easy editing, sculpting, rigging, animating, compositing and relighting of the Gaussians using traditional softwares by manipulating the mesh instead of the gaussians themselves. Retrieving such an editable mesh for realistic rendering is done within minutes with our method, compared to hours with the state-of-the-art methods on neural SDFs, while providing a better rendering quality. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.12775.pdf) | [🌐 Project Page](https://imagine.enpc.fr/~guedona/sugar/) | [💻 Code (not released yet)](https://github.com/Anttwo/SuGaR) 

## Regularization and Optimization:
### 1. Depth-Regularized Optimization for 3D Gaussian Splatting in Few-Shot Images 
**Authors**: Jaeyoung Chung, Jeongtaek Oh, Kyoung Mu Lee 
<details open>
<summary><b>Abstract</b></summary>
In this paper, we present a method to optimize Gaussian splatting with a limited number of images while avoiding overfitting. Representing a 3D scene by combining numerous Gaussian splats has yielded outstanding visual quality. However, it tends to overfit the training views when only a small number of images are available. To address this issue, we introduce a dense depth map as a geometry guide to mitigate overfitting. We obtained the depth map using a pre-trained monocular depth estimation model and aligning the scale and offset using sparse COLMAP feature points. The adjusted depth aids in the color-based optimization of 3D Gaussian splatting, mitigating floating artifacts, and ensuring adherence to geometric constraints. We verify the proposed method on the NeRF-LLFF dataset with varying numbers of few images. Our approach demonstrates robust geometry compared to the original method that relies solely on images. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.13398.pdf) 

### 2. Compact 3D Gaussian Representation for Radiance Field 
**Authors**: Joo Chan Lee, Daniel Rho, Xiangyu Sun, Jong Hwan Ko, Eunbyung Park 
<details open>
<summary><b>Abstract</b></summary>
Neural Radiance Fields (NeRFs) have demonstrated remarkable potential in capturing complex 3D scenes with high fidelity. However, one persistent challenge that hinders the widespread adoption of NeRFs is the computational bottleneck due to the volumetric rendering. On the other hand, 3D Gaussian splatting (3DGS) has recently emerged as an alternative representation that leverages a 3D Gaussisan-based representation and adopts the rasterization pipeline to render the images rather than volumetric rendering, achieving very fast rendering speed and promising image quality. However, a significant drawback arises as 3DGS entails a substantial number of 3D Gaussians to maintain the high fidelity of the rendered images, which requires a large amount of memory and storage. To address this critical issue, we place a specific emphasis on two key objectives: reducing the number of Gaussian points without sacrificing performance and compressing the Gaussian attributes, such as view-dependent color and covariance. To this end, we propose a learnable mask strategy that significantly reduces the number of Gaussians while preserving high performance. In addition, we propose a compact but effective representation of view-dependent color by employing a grid-based neural field rather than relying on spherical harmonics. Finally, we learn codebooks to compactly represent the geometric attributes of Gaussian by vector quantization. In our extensive experiments, we consistently show over 10× reduced storage and enhanced rendering speed, while maintaining the quality of the scene representation, compared to 3DGS. Our work provides a comprehensive framework for 3D scene representation, achieving high performance, fast training, compactness, and real-time rendering.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.13681.pdf) | [🌐 Project Page](https://maincold2.github.io/c3dgs/) | [💻 Code ](https://github.com/maincold2/Compact-3DGS) 

## 3D Gaussian Editing:
### 1. GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting 
**Authors**: Yiwen Chen, Zilong Chen, Chi Zhang, Feng Wang, Xiaofeng Yang, Yikai Wang, Zhongang Cai, Lei Yang, Huaping Liu, Guosheng Lin
<details open>
<summary><b>Abstract</b></summary>
3D editing plays a crucial role in many areas such as gaming and virtual reality. Traditional 3D editing methods, which rely on representations like meshes and point clouds, often fall short in realistically depicting complex scenes.
On the other hand, methods based on implicit 3D representations, like Neural Radiance Field (NeRF), render complex scenes effectively but suffer from slow processing speeds and limited control over specific scene areas. In response to these challenges, our paper presents GaussianEditor, an innovative and efficient 3D editing algorithm based on Gaussian Splatting (GS), a novel 3D representation technique.
GaussianEditor enhances precision and control in editing through our proposed Gaussian Semantic Tracing, which traces the editing target throughout the training process. Additionally, we propose hierarchical Gaussian splatting (HGS) to achieve stabilized and fine results under stochastic generative guidance from 2D diffusion models. We also develop editing strategies for efficient object removal and integration, a challenging task for existing methods. Our comprehensive experiments demonstrate GaussianEditor's superior control, efficacy, and rapid performance, marking a significant advancement in 3D editing.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.14521.pdf) | [🌐 Project Page](https://buaacyw.github.io/gaussian-editor/) | [💻 Code](https://github.com/buaacyw/GaussianEditor) | [🎥 Short Presentation](https://youtu.be/TdZIICSFqsU?si=-U4tyOvaAPqIROYn)

### 2. GaussianEditor: Editing 3D Gaussians Delicately with Text Instructions 
**Authors**: Jiemin Fang, Junjie Wang, Xiaopeng Zhang, Lingxi Xie, Qi Tian 
<details open>
<summary><b>Abstract</b></summary>
Recently, impressive results have been achieved in 3D scene editing with text instructions based on a 2D diffusion model. However, current diffusion models primarily generate images by predicting noise in the latent space, and the editing is usually applied to the whole image, which makes it challenging to perform delicate, especially localized, editing for 3D scenes. Inspired by recent 3D Gaussian splatting, we propose a systematic framework, named GaussianEditor, to edit 3D scenes delicately via 3D Gaussians with text instructions. Benefiting from the explicit property of 3D Gaussians, we design a series of techniques to achieve delicate editing. Specifically, we first extract the region of interest (RoI) corresponding to the text instruction, aligning it to 3D Gaussians. The Gaussian RoI is further used to control the editing process. Our framework can achieve more delicate and precise editing of 3D scenes than previous methods while enjoying much faster training speed, i.e. within 20 minutes on a single V100 GPU, more than twice as fast as Instruct-NeRF2NeRF (45 minutes -- 2 hours)
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.14521.pdf) | [🌐 Project Page](https://gaussianeditor.github.io/) | [💻 Code (not yet)]() | [🎥 Short Presentation](https://youtu.be/KWtALsigR3k?si=h6-A44brd5rm3_CM)


## 3D Gaussian Rendering:
### 1. Mip-Splatting Alias-free 3D Gaussian Splatting 
**Authors**: Zehao Yu, Anpei Chen, Binbin Huang, Torsten Sattler, Andreas Geiger
<details open>
<summary><b>Abstract</b></summary>
Recently, 3D Gaussian Splatting (3DGS) has demonstrated impressive novel view synthesis results, reaching high fidelity and efficiency. However, strong artifacts can be observed when changing the sampling rate, e.g., by changing focal length or camera distance. We find that the source for this phenomenon can be attributed to the lack of 3D frequency constraints and the usage of a 2D dilation filter. To address this problem, we introduce a 3D smoothing filter which constrains the size of the 3D Gaussian primitives based on the maximal sampling frequency induced by the input views, eliminating high frequency artifacts when zooming in. Moreover, replacing 2D dilation with a 2D Mip filter, which simulates a 2D box filter, effectively mitigates aliasing and dilation issues. Our comprehensive evaluation, including scenarios such as training on single-scale images and testing on multiple scales, validates the effectiveness of our approach. 
</details>

  [📄 Paper](https://drive.google.com/file/d/1Q7KgGbynzcIEyFJV1I17HgrYz6xrOwRJ/view) | [🌐 Project Page](https://niujinshuchong.github.io/mip-splatting/) | [💻 Code](https://github.com/autonomousvision/mip-splatting) 

### 2. Relightable 3D Gaussian: Real-time Point Cloud Relighting with BRDF Decomposition and Ray Tracing 
**Authors**: Jian Gao, Chun Gu, Youtian Lin, Hao Zhu, Xun Cao, Li Zhang, Yao Yao 
<details open>
<summary><b>Abstract</b></summary>
We present a novel differentiable point-based rendering framework for material and lighting decomposition from multi-view images, enabling editing, ray-tracing, and real-time relighting of the 3D point cloud. Specifically, a 3D scene is represented as a set of relightable 3D Gaussian points, where each point is additionally associated with a normal direction, BRDF parameters, and incident lights from different directions. To achieve robust lighting estimation, we further divide incident lights of each point into global and local components, as well as view-dependent visibilities. The 3D scene is optimized through the 3D Gaussian Splatting technique while BRDF and lighting are decomposed by physically-based differentiable rendering. Moreover, we introduce an innovative point-based ray-tracing approach based on the bounding volume hierarchy for efficient visibility baking, enabling real-time rendering and relighting of 3D Gaussian points with accurate shadow effects. Extensive experiments demonstrate improved BRDF estimation and novel view rendering results compared to state-of-the-art material estimation approaches. Our framework showcases the potential to revolutionize the mesh-based graphics pipeline with a relightable, traceable, and editable rendering pipeline solely based on point cloud.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.16043.pdf) | [🌐 Project Page](https://nju-3dv.github.io/projects/Relightable3DGaussian/) | [💻 Code (not yet)]() 

### 3. GS-IR: 3D Gaussian Splatting for Inverse Rendering 
**Authors**: Zhihao Liang, Qi Zhang, Ying Feng, Ying Shan, Kui Jia 
<details open>
<summary><b>Abstract</b></summary>
We propose GS-IR, a novel inverse rendering approach based on 3D Gaussian Splatting (GS) that leverages forward mapping volume rendering to achieve photorealistic novel view synthesis and relighting results. Unlike previous works that use implicit neural representations and volume rendering (e.g. NeRF), which suffer from low expressive power and high computational complexity, we extend GS, a top-performance representation for novel view synthesis, to estimate scene geometry, surface material, and environment illumination from multi-view images captured under unknown lighting conditions. There are two main problems when introducing GS to inverse rendering: 1) GS does not support producing plausible normal natively; 2) forward mapping (e.g. rasterization and splatting) cannot trace the occlusion like backward mapping (e.g. ray tracing). To address these challenges, our GS-IR proposes an efficient optimization scheme that incorporates a depth-derivation-based regularization for normal estimation and a baking-based occlusion to model indirect lighting. The flexible and expressive GS representation allows us to achieve fast and compact geometry reconstruction, photorealistic novel view synthesis, and effective physically-based rendering. We demonstrate the superiority of our method over baseline methods through qualitative and quantitative evaluations on various challenging scenes. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.16473.pdf) | [🌐 Project Page](https://github.com/lzhnb/GS-IR) | [💻 Code (not yet)](https://github.com/lzhnb/GS-IR) 


## Classic work:

### 1. A Generalization of Algebraic Surface Drawing
**Authors**: James F. Blinn

 ***Comment:***: First paper rendering 3D gaussians.

<details open>
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

<details open>
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

<details open>
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

<details open>
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
- [Unity Implementation](https://github.com/aras-p/UnityGaussianSplatting)
- [PlayCanvas Implementation](https://github.com/playcanvas/engine/tree/main/extras/splat)

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
- Thanks to [Henry Pearce](https://github.com/henrypearce4D) for adding more resources and debugging the video links.
