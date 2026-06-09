---
title: Five zomeable orthographic projections of the 6-cube
description: Five vZome models of orthographic 3D projections of the 6-dimensional cube, organized by symmetry.
image: https://www.nan.ma/vzome-sharing/2026/06/09/15-33-08-6_cube_red_H3/6_cube_red_H3.png
published: true
layout: vzome
---

<style>
  .six-cube-gallery {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
    margin: 2rem 0;
  }
  .six-cube-card {
    border: 1px solid #ddd;
    border-radius: 0.75rem;
    padding: 1rem;
    background: #fff;
    max-width: 60dvh;
    margin: 0 auto;
    width: 100%;
  }
  .six-cube-card vzome-viewer {
    display: block;
    width: 100%;
    aspect-ratio: 1 / 1;
    height: auto;
  }
  @media (min-width: 900px) {
    .six-cube-card vzome-viewer {
      margin: 0 auto;
    }
  }
  .six-cube-meta {
    margin: 0.75rem 0 0;
    color: #555;
    text-align: center;
  }
</style>

<div class="six-cube-gallery">
  <section class="six-cube-card">
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-33-08-6_cube_red_H3/6_cube_red_H3.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-33-08-6_cube_red_H3/6_cube_red_H3.png">
    </vzome-viewer>
    <p class="six-cube-meta">Red: full icosahedral symmetry (<code>H3 / Ih</code>).</p>
  </section>

  <section class="six-cube-card">
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-36-22-6_cube_green_2_Oh/6_cube_green_2_Oh.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-36-22-6_cube_green_2_Oh/6_cube_green_2_Oh.png">
    </vzome-viewer>
    <p class="six-cube-meta">Green 2: full octahedral symmetry (<code>Oh</code>).</p>
  </section>

  <section class="six-cube-card">
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-32-17-6_cube_yellow_paulo_Th/6_cube_yellow_paulo_Th.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-32-17-6_cube_yellow_paulo_Th/6_cube_yellow_paulo_Th.png">
    </vzome-viewer>
    <p class="six-cube-meta">Yellow: pyritohedral symmetry (<code>Th</code>).</p>
  </section>

  <section class="six-cube-card">
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-34-32-6_cube_blue_D3d/6_cube_blue_D3d.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-34-32-6_cube_blue_D3d/6_cube_blue_D3d.png">
    </vzome-viewer>
    <p class="six-cube-meta">Blue: dihedral three-fold symmetry with inversion (<code>D3d</code>).</p>
  </section>

  <section class="six-cube-card">
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-35-33-6_cube_green_1_C3i/6_cube_green_1_C3i.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-35-33-6_cube_green_1_C3i/6_cube_green_1_C3i.png">
    </vzome-viewer>
    <p class="six-cube-meta">Green 1: three-fold roto-inversion symmetry (<code>C3i / S6</code>).</p>
  </section>
</div>

These five models are zomeable orthographic projections of the 6-dimensional cube.  Each model is determined by six equal-length projected cube-edge vectors forming a tight frame in 3D.  Some projections identify multiple cube vertices or edges, so the visible model may be a collapsed projection of the abstract 6-cube.

| model | symmetry |
|---|---:|
| red | `H3 / Ih` |
| green 2 | `Oh` |
| yellow | `Th` |
| blue | `D3d` |
| green 1 | `C3i / S6` |

The final exported shapes were checked against their projected 6-cube edge skeletons, with no extra or missing visible struts.
