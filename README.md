# Mohamed Ashraf Fahmy — Portfolio

Static portfolio built with HTML, CSS, JavaScript, GSAP, ScrollTrigger, and Lenis. Includes six project case studies, a downloadable CV, and scroll animations.

## Run locally

From the project directory:

```powershell
python serve.py
```

Open [http://localhost:8000](http://localhost:8000). No package installation or build step is required.

`serve.py` is a plain static server that gzips text assets, so local numbers match real hosting. `python -m http.server 8000` also works, but it serves everything uncompressed.

## Files

- `index.html`: portfolio sections and project links.
- `style.css`: layout, animation styles, and the intro start states.
- `fonts.css` and `fonts/`: `@font-face` declarations and the woff2 files they point to.
- `main.js`: scrolling, animation, and case study viewer.
- `vendor/`: GSAP and ScrollTrigger scripts with their license notices.
- `work/`: MentoraX, LigoFlow, DawaBack, TolabExam, ElCargo and Taahud case studies and WebP screenshots (plus responsive sizes).
- `resume/Mohamed-Ashraf-Fahmy-CV.pdf`: the CV, linked from the contact section.
- `serve.py`: local preview server with gzip.

## Hosting

Serve this directory as a static website. Use the repository root as the source directory for GitHub Pages; no build command is needed.

GitHub: [moashraf41](https://github.com/moashraf41)
