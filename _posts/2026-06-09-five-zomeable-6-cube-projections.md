---
title: Five zomeable orthographic projections of the 6-cube
description: Five vZome models of orthographic 3D projections of the 6-dimensional cube, organized by symmetry.
image: https://www.nan.ma/vzome-sharing/2026/06/09/15-33-08-6_cube_red_H3/6_cube_red_H3.png
published: true
layout: vzome
---

These five models are zomeable orthographic projections of the 6-dimensional cube.  Each model is determined by six equal-length projected cube-edge vectors forming a tight frame in 3D.  Some projections identify multiple cube vertices or edges, so the visible ball and strut counts can be smaller than the abstract 6-cube's 64 vertices and 192 edges.

Paulo Freire independently created the pyritohedral yellow model.

| model | symmetry | visible balls | visible struts |
|---|---:|---:|---:|
| red | `H3 / Ih` | 64 | 192 |
| green 2 | `Oh` | 38 | 144 |
| yellow Paulo | `Th` | 64 | 192 |
| blue | `D3d` | 63 | 192 |
| green 1 | `C3i / S6` | 56 | 180 |

<style>
  .six-cube-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
  }
  .six-cube-card {
    border: 1px solid #ddd;
    border-radius: 0.75rem;
    padding: 1rem;
    background: #fff;
  }
  .six-cube-card h2 {
    margin-top: 0;
  }
  .six-cube-card vzome-viewer {
    width: 100%;
    height: 52dvh;
    min-height: 360px;
  }
  .six-cube-meta {
    margin: 0.5rem 0 0;
    color: #555;
  }
</style>

<div class="six-cube-gallery">
  <section class="six-cube-card">
    <h2>Red: H3 / Ih</h2>
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-33-08-6_cube_red_H3/6_cube_red_H3.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-33-08-6_cube_red_H3/6_cube_red_H3.png">
    </vzome-viewer>
    <p class="six-cube-meta">Full icosahedral symmetry; 64 balls and 192 struts.</p>
  </section>

  <section class="six-cube-card">
    <h2>Green 2: Oh</h2>
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-36-22-6_cube_green_2_Oh/6_cube_green_2_Oh.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-36-22-6_cube_green_2_Oh/6_cube_green_2_Oh.png">
    </vzome-viewer>
    <p class="six-cube-meta">Full octahedral symmetry; 38 visible balls and 144 visible struts after projection coincidences.</p>
  </section>

  <section class="six-cube-card">
    <h2>Yellow Paulo: Th</h2>
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-32-17-6_cube_yellow_paulo_Th/6_cube_yellow_paulo_Th.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-32-17-6_cube_yellow_paulo_Th/6_cube_yellow_paulo_Th.png">
    </vzome-viewer>
    <p class="six-cube-meta">Pyritohedral symmetry; 64 balls and 192 struts.  This is Paulo Freire's model.</p>
  </section>

  <section class="six-cube-card">
    <h2>Blue: D3d</h2>
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-34-32-6_cube_blue_D3d/6_cube_blue_D3d.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-34-32-6_cube_blue_D3d/6_cube_blue_D3d.png">
    </vzome-viewer>
    <p class="six-cube-meta">Dihedral 3-fold symmetry with inversion; 63 visible balls and 192 visible struts.</p>
  </section>

  <section class="six-cube-card">
    <h2>Green 1: C3i / S6</h2>
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-35-33-6_cube_green_1_C3i/6_cube_green_1_C3i.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-35-33-6_cube_green_1_C3i/6_cube_green_1_C3i.png">
    </vzome-viewer>
    <p class="six-cube-meta">Three-fold roto-inversion symmetry; 56 visible balls and 180 visible struts.</p>
  </section>
</div>

The final exported shapes were checked against their projected 6-cube edge skeletons: the visible ball and strut counts match the expected collapsed projections, with no extra or missing visible struts.
