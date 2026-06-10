---
title: Single-color equal-strut zomeable projections of the 6-cube
description: Five special orthographic 6-cube projections whose zome struts are single-colored and equal length.
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
    box-sizing: border-box;
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    padding: 0.25rem;
    background: #fff;
    max-width: min(100%, 72dvh);
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
    margin: 0.75rem 0 0.5rem;
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
    <p class="six-cube-meta">Green 1: three-fold roto-inversion symmetry (<code>C3i</code>).</p>
  </section>

  <section class="six-cube-card">
    <vzome-viewer src="https://www.nan.ma/vzome-sharing/2026/06/09/15-36-22-6_cube_green_2_Oh/6_cube_green_2_Oh.vZome">
      <img style="width: 100%" src="https://www.nan.ma/vzome-sharing/2026/06/09/15-36-22-6_cube_green_2_Oh/6_cube_green_2_Oh.png">
    </vzome-viewer>
    <p class="six-cube-meta">Green 2: full octahedral symmetry (<code>Oh</code>).</p>
  </section>
</div>

The 6-cube has infinitely many zomeable orthographic projections.  The five models here are special because each one uses struts of a single color, and all struts in the model have the same abstract length.

Each model is determined by six equal-length projected cube-edge vectors forming a tight frame in 3D.  Some projections identify multiple cube vertices or edges, so the visible model may be a collapsed projection of the abstract 6-cube.

| model | symmetry |
|---|---:|
| red | `H3 / Ih` |
| yellow | `Th` |
| blue | `D3d` |
| green 1 | `C3i` |
| green 2 | `Oh` |

We treat these as abstract strut graphs and ignore strut crossings as if they impose no physical constraint.  In a physical build, one might scale up the model and add balls at crossings, but that would change the equal-length property.  On this page, the original projected 6-cube edges are the objects of interest.

No additional 6-cube projections with both properties are currently known from this search.
