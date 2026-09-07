(() => {
  for (const viewer of document.querySelectorAll("vzome-viewer[data-scene-descriptions]")) {
    let scenes = [];
    let descriptionBox;

    const showDescription = (scene) => {
      const content = typeof scene?.content === "string" ? scene.content : "";
      if (!content.trim()) {
        descriptionBox?.remove();
        descriptionBox = undefined;
        return;
      }

      if (!descriptionBox) {
        descriptionBox = document.createElement("div");
        descriptionBox.className = "vzome-scene-description";
        descriptionBox.setAttribute("role", "note");
        descriptionBox.setAttribute("aria-label", "Scene description");
        descriptionBox.setAttribute("aria-live", "polite");
        descriptionBox.setAttribute("aria-atomic", "true");
        viewer.before(descriptionBox);
      }
      if (descriptionBox.textContent !== content) {
        descriptionBox.textContent = content;
      }
    };

    const selectedScene = (detail) => {
      if (Number.isInteger(detail?.index)) {
        return scenes[detail.index];
      }

      // Non-indexed render events omit the scene, so read the existing dropdown.
      const selector = viewer.shadowRoot?.querySelector("select.scene__select");
      const title = selector?.value ?? viewer.getAttribute("scene");
      if (title != null) {
        if (!title) return undefined;
        if (title.startsWith("#")) {
          return scenes[Number.parseInt(title.slice(1), 10) - 1];
        }
        return scenes.find((scene) => scene.title?.trim() === title.trim());
      }

      // The viewer does not create a dropdown when there is only one named scene.
      if (["named", "titled"].includes(viewer.getAttribute("show-scenes"))) {
        const namedScenes = scenes.filter((scene) => scene.title?.trim());
        if (namedScenes.length === 1) return namedScenes[0];
      }
      return undefined;
    };

    viewer.addEventListener("vzome-scenes", (event) => {
      scenes = event.detail;
      showDescription(selectedScene());
    });
    viewer.addEventListener("vzome-design-rendered", (event) => {
      showDescription(selectedScene(event.detail));
    });
    viewer.addEventListener("vzome-design-failed", () => {
      showDescription(undefined);
    });
  }
})();
