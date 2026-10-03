---
title: Perfectly Round Zome Models
date: 2026-08-02
share-description: Zometool models whose balls all lie at exactly the same distance from the centre.
image: exact_360.png
layout: vzome
---

Every model here is **perfectly round**: all of its balls sit at exactly the
same distance from the centre &mdash; equal in exact arithmetic, not merely
to within a tolerance &mdash; so they lie on a common sphere. Every edge of
the convex hull is a **single** standard strut. Drag to rotate any model.
For shells that are very round but not exactly so, see
[Approximate Zome Spheres](../../../07/26/approximate-zome-spheres/).

<script type='module' src='https://www.vzome.com/modules/vzome-viewer.js'></script>

<style>
  .approx-model {
    box-sizing: border-box;
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    background: #fff;
    margin: 2rem auto;
    max-width: min(100%, 72dvh);
    padding: 0.25rem;
    width: 100%;
  }
  .approx-model vzome-viewer {
    display: block;
    width: 100%;
    aspect-ratio: 1 / 1;
    height: auto;
  }
  .approx-model img {
    width: 100%;
    height: auto;
  }
  .approx-model figcaption {
    color: #24292f;
    margin: 0.75rem 0 0.5rem;
    text-align: center;
  }
  .approx-model figcaption .model-title {
    display: block;
    font-weight: 600;
  }
  .approx-model figcaption .model-note {
    color: #57606a;
    display: block;
    margin-top: 0.2rem;
  }
</style>

<figure class="approx-model">
 <vzome-viewer src="truncated_icosidodecahedron.vZome" progress="true" tween-duration="0" >
  <img src="truncated_icosidodecahedron.png" alt="Truncated icosidodecahedron - 120 balls 180 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">Truncated icosidodecahedron &mdash; 120 balls 180 struts</span>
  <span class="model-note">An Archimedean solid. All 120 balls lie in one orbit, so a common radius comes free from the symmetry.</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="ball_240_a.vZome" progress="true" tween-duration="0" >
  <img src="ball_240_a.png" alt="240 balls (variant a) 420 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">240 balls (variant a) 420 struts</span>
  <span class="model-note">Two orbits at a common radius.</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="ball_240_b.vZome" progress="true" tween-duration="0" >
  <img src="ball_240_b.png" alt="240 balls (variant b) 420 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">240 balls (variant b) 420 struts</span>
  <span class="model-note">Two orbits at a common radius.</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="ball_240_c.vZome" progress="true" tween-duration="0" >
  <img src="ball_240_c.png" alt="240 balls (variant c) 450 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">240 balls (variant c) 450 struts</span>
  <span class="model-note">Three orbits at a common radius.</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="exact_360.vZome" progress="true" tween-duration="0" >
  <img src="exact_360.png" alt="360 balls 600 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">360 balls 600 struts</span>
  <span class="model-note">Three orbits. Most balls with full icosahedral symmetry, struts of length 0-2.</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="exact_480_span3.vZome" progress="true" tween-duration="0" >
  <img src="exact_480_span3.png" alt="480 balls 720 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">480 balls 720 struts</span>
  <span class="model-note">Four orbits. Most balls with full icosahedral symmetry, struts of length 0-3.</span>
 </figcaption>
</figure>

## Physical construction

Scott Vorthmann and I built the **240-ball model, variant A**, shown in the
interactive gallery above. Its spherical shell has 240 balls and 420 struts.
The red struts support the model and are not part of the sphere.

<figure class="approx-model">
 <img src="physical-240-a-builders.jpg" alt="Two builders beside the completed blue-and-green 240-ball Zometool shell" loading="lazy" width="4032" height="3024">
 <figcaption>The completed 240-ball model, built by Nan Ma and Scott Vorthmann.</figcaption>
</figure>

<figure class="approx-model">
 <img src="physical-240-a-shell.jpg" alt="The 240-ball Zometool shell on the floor, with blue and green struts and red support legs" loading="lazy" width="2753" height="2753">
 <figcaption>A closer view of the shell.</figcaption>
</figure>

<figure class="approx-model">
 <img src="physical-240-a-suspended.jpg" alt="The blue-and-green 240-ball Zometool shell suspended from the ceiling" loading="lazy" width="2160" height="2880">
 <figcaption>The shell suspended from the ceiling.</figcaption>
</figure>
