# FOSDEM 2026 — Jellyfin Image Generation Prompts

Generated for use with **nanobanana** (or any text-to-image tool).
All images target a Jellyfin TV-series library layout as described in
`openspec/specs/video-download/spec.md`.

______________________________________________________________________

## Jellyfin Image Size Reference

| Image Type            | Jellyfin Filename                          | Dimensions (px) | Aspect Ratio   | Notes                                                      |
| --------------------- | ------------------------------------------ | --------------- | -------------- | ---------------------------------------------------------- |
| **Poster / Primary**  | `poster.png` (show) / `cover.png` (season) | **1000 × 1500** | 2:3 portrait   | Main artwork shown in library grid                         |
| **Backdrop / Fanart** | `backdrop.png`                             | **1920 × 1080** | 16:9 landscape | Background on detail pages                                 |
| **Banner**            | `banner.png`                               | **1000 × 185**  | ~5.4:1 wide    | Shown in banner browse mode                                |
| **Logo / Clearlogo**  | `logo.png`                                 | **800 × 310**   | ~2.6:1 wide    | Overlaid on backdrops; **transparent background** required |
| **Thumb / Landscape** | `thumb.png`                                | **960 × 540**   | 16:9 landscape | Thumbnail in list/thumb browse mode                        |

______________________________________________________________________

## Consistent Style Guide

### FOSDEM Brand Identity

The FOSDEM logo is a **rotary gear (cog wheel)** with **two circles
inside** that serve as eyes in the character version — giving the gear
a friendly, mascot-like personality. The official brand colour is a
distinctive **fuchsia-purple (#AF2C93)**.

### Colour Palette

| Role                           | Hex       | Swatch                                               | Notes                                                  |
| ------------------------------ | --------- | ---------------------------------------------------- | ------------------------------------------------------ |
| **Primary — FOSDEM Purple**    | `#AF2C93` | ![#AF2C93](https://placehold.co/20x20/AF2C93/AF2C93) | Main brand colour; use for key elements, titles, icons |
| **Secondary — Deep Plum**      | `#7B1F68` | ![#7B1F68](https://placehold.co/20x20/7B1F68/7B1F68) | Darker shade for depth, shadows, gradients             |
| **Accent — Soft Magenta**      | `#D64DB8` | ![#D64DB8](https://placehold.co/20x20/D64DB8/D64DB8) | Lighter tint for highlights and glows                  |
| **Background — Dark Charcoal** | `#1E1E1E` | ![#1E1E1E](https://placehold.co/20x20/1E1E1E/1E1E1E) | Base background for all images                         |
| **Text — White**               | `#FFFFFF` | ![#FFFFFF](https://placehold.co/20x20/FFFFFF/FFFFFF) | Primary text and line art                              |
| **Text — Light Grey**          | `#B0B0B0` | ![#B0B0B0](https://placehold.co/20x20/B0B0B0/B0B0B0) | Secondary/subtitle text                                |

### Visual Style

All prompts share these style directives to ensure visual consistency
across every generated image:

> **Style keywords (append to every prompt):**
> Hand-drawn illustration style with visible ink-line texture, as if
> sketched with a fine-tip marker and then digitally coloured.
> Clean geometric shapes with slightly organic hand-drawn edges.
> Bold solid colours from the FOSDEM palette: fuchsia-purple (#AF2C93)
> as the primary accent, deep plum (#7B1F68) for shadows/depth, soft
> magenta (#D64DB8) for highlights and glows, white (#FFFFFF) for line
> art and text, light grey (#B0B0B0) for secondary elements.
> Dark charcoal (#1E1E1E) background.
> Subtle crosshatch or stipple texture in backgrounds (like a
> hand-drawn technical illustration). No photographic elements.
> No heavy gradients — only subtle shading to suggest depth.
> Modern tech-conference aesthetic with a whimsical, approachable feel
> (inspired by the FOSDEM gear-with-eyes mascot). High contrast,
> sharp but slightly imperfect edges (hand-drawn look). Minimal detail,
> suitable for display on a TV media-centre interface.
> Include a small FOSDEM gear-with-eyes motif as a subtle watermark
> or corner emblem where appropriate.

______________________________________________________________________

## Show-Level Images (FOSDEM 2026)

These go into `Fosdem (2026)/`.

### Show Poster — `poster.png`

**Size:** 1000 × 1500 px

> A vertical poster for "FOSDEM 2026" — the premier European open-source
> developer conference held in Brussels. Centre a large FOSDEM gear-cog
> logo with two circular "eyes" inside, giving it a friendly mascot
> personality. The gear is drawn in a hand-sketched ink-line style with
> FOSDEM purple (#AF2C93) fill. Above: bold text "FOSDEM". Below: "2026"
> and "Brussels" in smaller type. Dark charcoal (#1E1E1E) background
> with subtle crosshatch texture. Hand-drawn illustration style,
> no photographs.
>
> **Dimensions: 1000 × 1500 pixels. Output format: PNG.**

### Show Backdrop — `backdrop.png`

**Size:** 1920 × 1080 px

> A wide cinematic backdrop for "FOSDEM 2026". Panoramic view of a
> stylised Brussels skyline (Atomium silhouette, university buildings)
> drawn in hand-sketched ink-line style. Foreground: an abstract
> circuit-board pattern radiating outward. Colour palette: dark charcoal
> (#1E1E1E) base, FOSDEM purple (#AF2C93) highlights on the skyline,
> soft magenta (#D64DB8) glow accents, white ink lines. Subtle
> crosshatch texture overlay. No text. No photographic elements.
>
> **Dimensions: 1920 × 1080 pixels. Output format: PNG.**

### Show Banner — `banner.png`

**Size:** 1000 × 185 px

> A wide horizontal banner for "FOSDEM 2026". Left side: small FOSDEM
> gear-with-eyes mascot icon in FOSDEM purple (#AF2C93). Centre: bold
> text "FOSDEM 2026" in white. Right side: subtle hand-drawn
> circuit-trace decorative lines trailing off in soft magenta (#D64DB8).
> Dark charcoal (#1E1E1E) background with crosshatch texture.
> Hand-drawn illustration style, no photographs, slightly organic edges.
>
> **Dimensions: 1000 × 185 pixels. Output format: PNG.**

### Show Logo — `logo.png`

**Size:** 800 × 310 px

> A clearlogo for "FOSDEM 2026" on a **fully transparent background**.
> The word "FOSDEM" in bold geometric sans-serif, FOSDEM purple
> (#AF2C93). "2026" in a lighter weight, white. The letter "O" is
> replaced by the FOSDEM gear-cog logo with two circular eyes inside.
> Hand-drawn ink-line style, no background, no drop shadow, slightly
> organic edges.
>
> **Dimensions: 800 × 310 pixels. Output format: PNG with transparency.**

### Show Thumb — `thumb.png`

**Size:** 960 × 540 px

> A landscape thumbnail for "FOSDEM 2026". A stylised top-down view of
> a packed conference hall drawn in hand-sketched ink-line style with
> rows of small circles (attendees). Stage at the front with a purple
> (#AF2C93) glow. Text "FOSDEM 2026" in the upper-left corner. Dark
> charcoal (#1E1E1E) background, FOSDEM purple and soft magenta
> (#D64DB8) accents, crosshatch texture. No photographs.
>
> **Dimensions: 960 × 540 pixels. Output format: PNG.**

______________________________________________________________________

## Season-Level Images (Per Track)

These go into `Fosdem (2026)/<Track Name>/`.
Each track needs **5 images**: poster (cover), backdrop, banner, logo, thumb.

Below are prompts for all 72 FOSDEM 2026 tracks. Each subsection
contains all 5 image type prompts.

______________________________________________________________________

### /dev/random

**Cover (poster)** — 1000 × 1500 px

> A vertical poster for the "/dev/random" track at FOSDEM 2026. A
> stylised old-fashioned slot machine or dice made of circuit-board
> traces, symbolising randomness and the unexpected. "dev/random" text
> at bottom. FOSDEM purple accent, dark charcoal background,
> hand-drawn illustration, crosshatch texture, no photographs.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop for "/dev/random". Abstract pattern of random geometric
> shapes — triangles, circles, squares — scattered across frame in
> varying sizes. FOSDEM purple and white on dark charcoal. Hand-drawn illustration,
> crosshatch overlay. No text, no photos.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner for "/dev/random". Left: dice icon in FOSDEM purple (#AF2C93). Centre:
> bold text "/dev/random". Dark charcoal background, crosshatch texture,
> hand-drawn illustration. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo for "/dev/random" on **transparent background**. Text
> "/dev/random" in bold monospace font, FOSDEM purple. Small dice icon.
> No background. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumbnail for "/dev/random". Collage of random tech icons —
> gears, terminals, dice, question marks — in hand-drawn illustration. FOSDEM
> purple and white on dark charcoal. Crosshatch texture.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### AI Plumbers

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "AI Plumbers" track. A stylised robot holding a
> wrench, with neural-network node patterns flowing from the wrench like
> water pipes. "AI Plumbers" text at bottom. FOSDEM purple accent, dark
> charcoal background, hand-drawn ink-line illustration, crosshatch texture.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop for "AI Plumbers". Abstract neural network graph
> connected by pipe-like conduits. Nodes glow in FOSDEM purple, pipes in
> white. Dark charcoal background. Hand-drawn illustration, crosshatch overlay. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner for "AI Plumbers". Left: brain-with-wrench icon in
> purple. Centre: bold text "AI Plumbers". Hand-drawn illustration, dark charcoal,
> crosshatch. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo for "AI Plumbers" on **transparent background**. "AI" in bold
> purple, "Plumbers" in white. Wrench icon integrated into the letter A.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumbnail for "AI Plumbers". Pipe system carrying data
> streams (ones and zeros) between neural-network nodes. Hand-drawn illustration,
> FOSDEM purple and white on dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Audio, Video & Graphics Creation

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Audio, Video & Graphics Creation" track. A
> stylised vector composition: sound waveform, film strip, and colour
> palette arranged vertically. FOSDEM purple, dark charcoal, hand-drawn illustration,
> crosshatch texture. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: abstract audio waveforms merging into video frames
> merging into paint brush strokes. All in hand-drawn illustration, FOSDEM purple
> and white on dark charcoal. No text, crosshatch overlay.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: speaker+film+brush combo icon. Centre:
> "Audio, Video & Graphics". Hand-drawn illustration, dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "AVG" monogram with waveform
> integrated. FOSDEM purple. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: split into three panels — audio waveform, video play
> button, colour wheel. Hand-drawn illustration, FOSDEM purple accents, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Bioinformatics & Computational Biology

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Bioinformatics & Computational Biology". A
> stylised DNA double helix made of circuit traces and binary code.
> FOSDEM purple helix, dark charcoal background, hand-drawn illustration, crosshatch.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: flowing DNA strands merging into data streams and graph
> charts. Hand-drawn illustration, FOSDEM purple and white nodes on dark charcoal.
> No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: DNA helix icon in FOSDEM purple (#AF2C93). Centre: bold text
> "Bioinformatics". Hand-drawn illustration, dark charcoal, crosshatch texture.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Bio" in FOSDEM purple (#AF2C93), "informatics"
> in white. DNA icon integrated. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumbnail: microscope view with geometric cell structures
> connected by data flow lines. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### BOF/Unconference

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "BOF/Unconference". Stylised circle of chairs
> (birds-of-a-feather meeting) rendered as geometric shapes. Speech
> bubbles emerging from the circle. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: abstract connected speech bubbles forming a network
> graph. Orange and white on dark charcoal. No text. Hand-drawn illustration,
> crosshatch. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: speech-bubble cluster icon. Centre:
> "BOF / Unconference". Dark charcoal, FOSDEM purple, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "BOF" in bold purple. Slash
> and "Unconference" in white. Speech bubble icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: round-table discussion scene, stylised people icons
> in a circle. Hand-drawn illustration, FOSDEM purple highlights, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Browser and web platform

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Browser and web platform". A stylised browser
> window frame with HTML tags floating inside. Globe icon in centre.
> FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: cascading HTML/CSS/JS code snippets rendered as hand-drawn
> geometric blocks, connected by web-like thread lines. FOSDEM purple
> and white, dark charcoal. No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: globe-in-browser icon. Centre: "Browser & Web
> Platform". Hand-drawn illustration, dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Web" in FOSDEM purple (#AF2C93) bold,
> "Platform" in white. Browser-tab icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: stylised browser tabs showing different web
> technologies. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### BSD, illumos, bhyve, OpenZFS

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "BSD, illumos, bhyve, OpenZFS". Stylised BSD
> daemon silhouette combined with a storage disk array icon. FOSDEM
> purple, dark charcoal, hand-drawn ink-line illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: layered storage volumes rendered as stacked geometric
> rectangles, with a daemon silhouette emerging. Orange and white on
> dark charcoal. No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: daemon icon. Centre: "BSD / illumos / OpenZFS".
> Dark charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "BSD" in FOSDEM purple (#AF2C93) bold. Daemon
> trident icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: four icons in a row — BSD daemon, sun (illumos), bee
> (bhyve), disk stack (ZFS). Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Building Europe's Public Digital Infrastructure

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Building Europe's Public Digital Infrastructure".
> Map outline of Europe made of digital circuit-board traces. Key
> cities marked as glowing purple nodes. Dark charcoal background,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: abstract Europe map with network connections between
> nodes. FOSDEM purple lines, white node dots, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: EU star circle icon in FOSDEM purple (#AF2C93). Centre:
> "EU Digital Infrastructure". Dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "EU Digital" in FOSDEM purple (#AF2C93),
> "Infrastructure" in white. EU stars icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: stylised European parliament building connected by
> digital data streams. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Collaboration and content management

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Collaboration and content management". Multiple
> document icons interconnected by arrows, with user silhouettes
> collaborating. FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: overlapping document layers with connecting arrows and
> user icons. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: people+document icon. Centre: "Collaboration
> & CMS". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Collab" in FOSDEM purple (#AF2C93), "CMS" in
> white. Document-share icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: kanban board with cards being moved by stylised
> cursor hands. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Community

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Community" track. Circle of diverse stylised
> human silhouettes holding hands, rendered as geometric shapes. FOSDEM
> purple accents, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: interconnected people icons forming a large network
> graph. Orange and white nodes, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: group-of-people icon. Centre: "Community".
> Dark charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Community" in FOSDEM purple (#AF2C93) bold.
> Heart + people icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: crowd of stylised people icons in a conference hall
> layout. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Confidential Computing

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Confidential Computing". A stylised padlock with
> a CPU chip inside, surrounded by encryption symbols. FOSDEM purple,
> dark charcoal, hand-drawn ink-line illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: array of encrypted data blocks (hex patterns) with a
> glowing secure enclave at centre. Orange and white on dark charcoal.
> No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: shield+chip icon. Centre: "Confidential
> Computing". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Confidential" in FOSDEM purple (#AF2C93),
> "Computing" in white. Shield icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: CPU die surrounded by a protective shield bubble.
> Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Containers

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Containers" track. Stacked shipping containers
> rendered as hand-drawn geometric blocks with tech labels. FOSDEM purple
> containers, dark charcoal background, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: port crane lifting containers that have circuit-board
> patterns. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: container box icon. Centre: "Containers".
> Dark charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Containers" in FOSDEM purple (#AF2C93).
> Stacked-boxes icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: row of containers on a conveyor belt with
> orchestration arrows. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### CRA in practice

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "CRA in practice" (Cyber Resilience Act). A
> stylised EU regulation document with a shield and checkmark. FOSDEM
> purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: checklist document overlaid on a circuit-board pattern
> with EU star ring. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: shield+document icon. Centre: "CRA in
> Practice". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "CRA" in FOSDEM purple (#AF2C93) bold,
> "in practice" in white. Compliance checkmark icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: compliance checklist with green checkmarks on an
> purple-accented dark background. Hand-drawn illustration.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Databases

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Databases". A stylised database cylinder with
> data tables and SQL symbols flowing in/out. FOSDEM purple, dark
> charcoal, hand-drawn ink-line illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: multiple database cylinders connected by query arrows
> and data streams. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: database cylinder icon. Centre: "Databases".
> Dark charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Databases" in FOSDEM purple (#AF2C93).
> Cylinder icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: table grid with data rows and JOIN diagram. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Decentralised Communication

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Decentralised Communication". A mesh network of
> chat-bubble nodes with no central hub. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: distributed mesh of speech-bubble nodes connected by
> peer-to-peer lines. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: mesh-network icon. Centre: "Decentralised
> Communication". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Decentral" in FOSDEM purple (#AF2C93),
> "Comm" in white. Mesh node icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: world map with distributed chat nodes connected
> across continents. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Decentralized Internet and Privacy

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Decentralized Internet and Privacy". A globe
> wrapped in a privacy shield with distributed network nodes. FOSDEM
> purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: abstract internet topology with shield-protected nodes.
> Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: shield+globe icon. Centre: "Decentralized
> Internet & Privacy". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Privacy" in FOSDEM purple (#AF2C93), "Web"
> in white. Padlock+globe icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: onion-layered privacy network diagram. Hand-drawn illustration,
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Declarative and Minimalistic Computing

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Declarative and Minimalistic Computing". A single
> elegant function symbol (lambda or arrow) on a zen-like minimalist
> canvas. FOSDEM purple on dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: sparse, perfectly balanced geometric composition — few
> shapes, lots of empty space. Orange accents on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: lambda icon. Centre: "Declarative Computing".
> Minimalist, dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Declarative" in FOSDEM purple (#AF2C93) thin
> type. Lambda symbol. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: clean code block with just three lines of declarative
> syntax. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Distributions

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Distributions". Multiple Linux distro logos
> abstracted as geometric shapes arranged in a grid. FOSDEM purple,
> dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: branching tree diagram representing distro family
> trees. Orange branches, white leaves, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: package-box icon. Centre: "Distributions".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Distros" in FOSDEM purple (#AF2C93). Branching
> tree icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: grid of abstract OS logos in hand-drawn illustration style.
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### DNS

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "DNS". A large stylised magnifying glass over a
> domain name hierarchy tree. FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: hierarchical tree of domain zones (.com, .org, .net)
> connected by resolver arrows. Orange and white on dark charcoal.
> No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: globe+magnifier icon. Centre: "DNS". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "DNS" in FOSDEM purple (#AF2C93) bold
> monospace. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: DNS query flow diagram — client, resolver, root,
> authoritative. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### eBPF

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "eBPF". A stylised kernel space with a bee icon
> (eBPF mascot) tracing through it. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: cross-section of Linux kernel layers with eBPF probe
> points glowing in FOSDEM purple (#AF2C93). Dark charcoal, hand-drawn ink-line illustration. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: bee icon. Centre: "eBPF". Dark charcoal,
> FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "eBPF" in FOSDEM purple (#AF2C93). Bee icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: eBPF program flow from userspace through verifier to
> kernel hooks. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Educational

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Educational". Stylised graduation cap on a
> computer monitor with coding symbols. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: chalkboard with tech diagrams and code snippets. Orange
> chalk highlights, dark charcoal board. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: graduation-cap icon. Centre: "Educational".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Edu" in FOSDEM purple (#AF2C93), graduation
> cap icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: classroom with screens showing code tutorials. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Embedded, Mobile and Automotive

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Embedded, Mobile and Automotive". Three icons
> stacked: microcontroller chip, smartphone, car dashboard. FOSDEM
> purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: PCB board layout morphing into a car dashboard and
> smartphone screen. Orange traces, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: chip+car icon. Centre: "Embedded & Mobile &
> Auto". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Embedded" in FOSDEM purple (#AF2C93). Chip
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: split panel — embedded board, phone, car. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Energy

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Energy" track. Stylised power grid with wind
> turbines and solar panels connected by smart-grid data lines. FOSDEM
> purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: energy landscape — wind turbines, solar panels,
> transmission towers connected by data streams. Orange and white on
> dark charcoal. No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: lightning-bolt icon. Centre: "Energy". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Energy" in FOSDEM purple (#AF2C93).
> Lightning bolt icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: smart energy grid diagram. Hand-drawn illustration, FOSDEM
> purple, dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### FOSS on Mobile

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "FOSS on Mobile". Stylised smartphone displaying
> open-source logos (FOSS heart icon) on screen. FOSDEM purple, dark
> charcoal, hand-drawn ink-line illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: grid of mobile app icons all with FOSS/open-source
> symbols. Orange accents, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: phone+heart icon. Centre: "FOSS on Mobile".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "FOSS" in FOSDEM purple (#AF2C93), "Mobile"
> in white. Phone icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: two smartphones side-by-side running FOSS apps. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### FPGA and VLSI

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "FPGA and VLSI". Close-up of a stylised FPGA die
> with configurable logic blocks highlighted. FOSDEM purple, dark
> charcoal, hand-drawn ink-line illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: chip floor-plan layout with logic gates and routing
> channels. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: chip-die icon. Centre: "FPGA & VLSI". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "FPGA" in FOSDEM purple (#AF2C93) bold.
> Logic-gate icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: FPGA routing diagram with LUTs and interconnects.
> Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Funding the FOSS Ecosystem

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Funding the FOSS Ecosystem". A tree made of
> code brackets with coins as leaves/fruit. FOSDEM purple, dark
> charcoal, hand-drawn ink-line illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: flowing river of coins feeding into an open-source
> garden of growing projects. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: coin+code icon. Centre: "Funding FOSS". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Fund" in FOSDEM purple (#AF2C93), "FOSS" in
> white. Coin-with-heart icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: donation pipeline flowing to multiple FOSS project
> icons. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Gaming and VR devroom

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Gaming and VR devroom". Stylised game controller
> merging into a VR headset. FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: abstract virtual-reality grid landscape with game
> elements (polygonal mountains, pixelated trees). Orange and white on
> dark charcoal. No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: gamepad icon. Centre: "Gaming & VR". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Gaming" in FOSDEM purple (#AF2C93), "VR" in
> white. VR headset icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: split screen — retro pixel game on left, VR world
> on right. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### GCC (GNU Toolchain)

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "GCC (GNU Toolchain)". Stylised GNU wildebeest
> head with compiler pipeline (source → AST → binary) flowing through.
> FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: compilation pipeline stages as connected geometric
> blocks. Orange arrows, white blocks, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: GNU head icon. Centre: "GCC / GNU Toolchain".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "GCC" in FOSDEM purple (#AF2C93) bold
> monospace. GNU icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: code compilation flow diagram. Hand-drawn illustration, FOSDEM
> purple, dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Geospatial

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Geospatial". Stylised topographic map with
> contour lines and a location pin. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: satellite view of terrain rendered as hand-drawn geometric
> elevation layers. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: map-pin icon. Centre: "Geospatial". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Geo" in FOSDEM purple (#AF2C93). Globe+pin
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: GIS map layers stacked transparently. Hand-drawn illustration,
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Go

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Go" track. Stylised Go gopher mascot rendered
> in hand-drawn geometric style. FOSDEM purple tinted gopher, dark
> charcoal background. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: abstract goroutine concurrency diagram — multiple
> channels flowing between parallel goroutine blocks. Orange and white
> on dark charcoal. No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: gopher icon. Centre: "Go". Dark charcoal,
> FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Go" in bold purple. Gopher
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: Go code snippet with goroutines visualised. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Graphics

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Graphics". Stylised GPU with rendering pipeline
> stages — vertex, rasterise, fragment. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: wireframe 3D scene being rendered — mesh → shaded →
> final. Orange wireframes, white shading, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: GPU/triangle icon. Centre: "Graphics". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Graphics" in FOSDEM purple (#AF2C93). 3D
> cube wireframe icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: rendering pipeline diagram. Hand-drawn illustration, FOSDEM
> purple, dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### HPC, Big Data & Data Science

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "HPC, Big Data & Data Science". Stylised
> supercomputer rack with data flowing into analysis charts. FOSDEM
> purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: cluster of server racks with data visualisation charts
> and graphs emerging. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: server-cluster icon. Centre: "HPC & Big
> Data". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "HPC" in FOSDEM purple (#AF2C93) bold.
> Bar-chart icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: data pipeline from raw data through processing to
> charts. Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Identity and Access Management

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Identity and Access Management". Stylised key
> and fingerprint combined into one icon. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: identity credential cards flowing through access
> gates. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: key+fingerprint icon. Centre: "IAM". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "IAM" in FOSDEM purple (#AF2C93). Key icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: authentication flow diagram (login → MFA → access).
> Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Junior

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Junior" track. Young person silhouette at a
> computer with code stars and lightbulbs. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: playful coding blocks and rockets launching. Orange
> and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: rocket+star icon. Centre: "Junior". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Junior" in FOSDEM purple (#AF2C93). Star
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: kids-friendly coding workshop scene in hand-drawn illustration.
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Kernel

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Kernel" track. Stylised Tux penguin at the
> centre of concentric kernel-space rings (syscalls, drivers, core).
> FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: concentric rings representing kernel layers from core
> to userspace. Orange inner rings, fading outward. Dark charcoal.
> No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: Tux icon. Centre: "Kernel". Dark charcoal,
> FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Kernel" in FOSDEM purple (#AF2C93). Tux
> silhouette. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: kernel subsystem diagram. Hand-drawn illustration, FOSDEM purple,
> dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Legal & Policy

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Legal & Policy". Stylised scales of justice with
> open-source logos on the pans. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: law books morphing into code licenses. Orange and white
> on dark charcoal. No text. **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: gavel icon. Centre: "Legal & Policy". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Legal" in FOSDEM purple (#AF2C93). Scales
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: license document with FOSS logos. Hand-drawn illustration,
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### LLVM

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "LLVM". Stylised dragon (LLVM mascot) wrapped
> around compiler IR code blocks. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: LLVM IR code blocks flowing through optimisation
> passes. Orange highlights, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: dragon icon. Centre: "LLVM". Dark charcoal,
> FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "LLVM" in FOSDEM purple (#AF2C93) bold
> monospace. Dragon silhouette.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: compiler pipeline — frontend → IR → backend. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Local-First, sync engines, CRDTs

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Local-First, sync engines, CRDTs". Two devices
> syncing data with merge arrows between them. FOSDEM purple, dark
> charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: multiple devices with bidirectional sync arrows forming
> a mesh. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: sync-arrows icon. Centre: "Local-First &
> CRDTs". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Local-First" in FOSDEM purple (#AF2C93).
> Sync icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: CRDT merge diagram with conflict resolution. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Main Track

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Main Track". Bold FOSDEM logo with stage
> spotlight beams. "Main Track" subtitle. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: grand auditorium silhouette with spotlights and a large
> screen. Orange glow, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: stage icon. Centre: "Main Track". Dark
> charcoal, FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Main Track" in FOSDEM purple (#AF2C93) bold.
> Spotlight icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: large lecture hall from back-of-room perspective.
> Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Main Track (K-building)

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Main Track (K-building)". Similar to Main Track
> but with a "K" badge overlaid on the auditorium. FOSDEM purple, dark
> charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: K-building auditorium with tiered seating and large
> screen. Orange spotlights, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: "K" badge icon. Centre: "Main Track (K)".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Main K" in FOSDEM purple (#AF2C93). Building
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: K-building auditorium wide angle. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Microkernel and Component-Based OS

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Microkernel and Component-Based OS". Tiny kernel
> core surrounded by modular component blocks connected by IPC arrows.
> FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: minimal kernel core with satellite component services.
> Orange core, white components, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: kernel-core icon. Centre: "Microkernel OS".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "uKernel" in FOSDEM purple (#AF2C93). Tiny
> core icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: microkernel architecture diagram. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Modern Email

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Modern Email". Stylised envelope transforming
> into a modern encrypted message with JMAP/IMAP protocol labels.
> FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: email flow — compose → encrypt → deliver → inbox.
> Orange arrows, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: envelope icon. Centre: "Modern Email". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Email" in FOSDEM purple (#AF2C93). Envelope
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: email protocols diagram. Hand-drawn illustration, FOSDEM purple,
> dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Music Production

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Music Production". Stylised mixing console with
> sliders and a waveform display. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: DAW interface with tracks, mixer, and waveforms. Orange
> highlights, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: musical-note icon. Centre: "Music Production".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Music" in FOSDEM purple (#AF2C93). Note icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: audio waveform and MIDI piano roll. Hand-drawn illustration,
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Network

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Network" track. Stylised network topology —
> routers, switches, and links forming a tree. FOSDEM purple, dark
> charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: abstract network mesh with routers and packet flows.
> Orange nodes, white links, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: network-node icon. Centre: "Network". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Network" in FOSDEM purple (#AF2C93). Router
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: OSI layer diagram. Hand-drawn illustration, FOSDEM purple, dark
> charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Nix and NixOS

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Nix and NixOS". Stylised Nix snowflake logo
> made of geometric hexagonal shapes. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: derivation graph — interconnected package nodes
> forming a DAG. Orange nodes, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: snowflake icon. Centre: "Nix & NixOS". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Nix" in FOSDEM purple (#AF2C93). Snowflake
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: Nix build graph. Hand-drawn illustration, FOSDEM purple, dark
> charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Open Hardware and CAD/CAM

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Open Hardware and CAD/CAM". Open-source gear
> icon combined with a CAD drawing outline. FOSDEM purple, dark
> charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: technical CAD blueprint with component outlines and
> measurements. Orange lines, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: gear+ruler icon. Centre: "Open Hardware &
> CAD". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "OpenHW" in FOSDEM purple (#AF2C93). Gear
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: PCB layout next to 3D CAD model. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Open Media devroom

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Open Media devroom". Film reel, headphones, and
> play button composed into a single icon. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: streaming media — video frames, audio waves, codec
> blocks flowing. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: play-button icon. Centre: "Open Media". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Open Media" in FOSDEM purple (#AF2C93).
> Play icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: media codec pipeline diagram. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Open Research

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Open Research". Stylised open book with
> scientific graphs and formulas emerging from pages. FOSDEM purple,
> dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: interconnected research paper nodes forming a citation
> graph. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: open-book icon. Centre: "Open Research".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Open Research" in FOSDEM purple (#AF2C93).
> Microscope icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: research paper with data visualisations. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Open Source Design

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Open Source Design". Pen tool and colour palette
> icons arranged artistically. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: design workspace with vector paths, colour swatches,
> and typography samples. Orange accents, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: pen-tool icon. Centre: "Open Source Design".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Design" in FOSDEM purple (#AF2C93). Pen-tool
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: UI/UX wireframe mockups. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Open Source Digital Forensics

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Open Source Digital Forensics". Magnifying glass
> over a hard drive with binary fingerprint patterns. FOSDEM purple,
> dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: forensic analysis timeline with evidence nodes and
> hash values. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: magnifier+disk icon. Centre: "Digital
> Forensics". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Forensics" in FOSDEM purple (#AF2C93).
> Magnifier icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: evidence chain diagram. Hand-drawn illustration, FOSDEM purple,
> dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Open Source & EU Policy

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Open Source & EU Policy". EU flag stars arranged
> around an open-source heart icon. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: EU parliament silhouette with open-source code flowing
> through it. Orange accents, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: EU+code icon. Centre: "Open Source & EU
> Policy". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "EU Policy" in FOSDEM purple (#AF2C93). EU
> stars icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: policy document with code brackets. Hand-drawn illustration,
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Package Management

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Package Management". Stylised package boxes with
> dependency arrows between them. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: dependency graph of packages with version labels.
> Orange nodes, white arrows, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: package icon. Centre: "Package Management".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Packages" in FOSDEM purple (#AF2C93). Box
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: package dependency tree. Hand-drawn illustration, FOSDEM purple,
> dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Plan 9

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Plan 9". Stylised Glenda bunny (Plan 9 mascot)
> in hand-drawn geometric style. FOSDEM purple, dark charcoal.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: Plan 9 namespace tree with mounted resources. Orange
> and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: bunny icon. Centre: "Plan 9". Dark charcoal,
> FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Plan 9" in FOSDEM purple (#AF2C93). Bunny
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: Plan 9 filesystem namespace diagram. Hand-drawn illustration,
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Python

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Python" track. Two intertwined snakes forming
> the Python logo in geometric style. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: Python code blocks flowing through an interpreter
> pipeline. Orange syntax highlights, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: Python snake icon. Centre: "Python". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Python" in FOSDEM purple (#AF2C93). Snake
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: Python REPL with code. Hand-drawn illustration, FOSDEM purple,
> dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Railways and Open Transport

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Railways and Open Transport". Stylised train
> on tracks with open-data signal towers. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: railway network map with real-time data overlays.
> Orange tracks, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: train icon. Centre: "Railways & Open
> Transport". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Rail" in FOSDEM purple (#AF2C93). Train icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: train timetable display with real-time data. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Retrocomputing

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Retrocomputing". Stylised vintage CRT monitor
> with green phosphor text. FOSDEM purple accents, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: retro 8-bit pixel landscape with vintage computers.
> Orange and green accents, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: CRT monitor icon. Centre: "Retrocomputing".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Retro" in FOSDEM purple (#AF2C93) pixel
> font. CRT icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: collection of vintage computers and floppy disks.
> Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### RISC-V

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "RISC-V". The RISC-V wordmark stylised with
> circuit-board traces emanating from it. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: RISC-V instruction pipeline diagram (fetch, decode,
> execute). Orange blocks, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: chip icon. Centre: "RISC-V". Dark charcoal,
> FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "RISC-V" in FOSDEM purple (#AF2C93) bold.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: RISC-V core block diagram. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Robotics and Simulation

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Robotics and Simulation". Stylised robot arm in
> a simulation grid environment. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: physics simulation grid with robot models moving.
> Orange highlights, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: robot arm icon. Centre: "Robotics & Sim".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Robotics" in FOSDEM purple (#AF2C93). Robot
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: simulated robot in a virtual world. Hand-drawn illustration,
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Rust

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Rust" track. Stylised Rust gear-crab mascot
> (Ferris) in hand-drawn geometric style. FOSDEM purple, dark charcoal.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: ownership and borrowing diagram with arrows and scopes.
> Orange highlights, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: Ferris crab icon. Centre: "Rust". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Rust" in FOSDEM purple (#AF2C93). Gear icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: Rust code with borrow checker annotations. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### SBOMS and supply chains

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "SBOMS and supply chains". A bill-of-materials
> document with linked component boxes. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: software supply chain pipeline with SBOM checkpoints.
> Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: chain-link icon. Centre: "SBOMs & Supply
> Chains". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "SBOM" in FOSDEM purple (#AF2C93). Chain
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: supply chain graph with verification checkmarks.
> Hand-drawn illustration, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Search

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Search". Stylised magnifying glass over an
> inverted index data structure. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: search index with documents being crawled and ranked.
> Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: search icon. Centre: "Search". Dark charcoal,
> FOSDEM purple. **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Search" in FOSDEM purple (#AF2C93).
> Magnifier icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: search results page with relevance scoring. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Security

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Security". Stylised shield with a lock and
> binary code background. FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: layered security architecture — firewall, IDS,
> encryption. Orange shields, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: shield icon. Centre: "Security". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Security" in FOSDEM purple (#AF2C93). Shield
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: security audit dashboard. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Social Web

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Social Web". Interconnected user profile icons
> with ActivityPub/Fediverse connections. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: federated social network graph with server instances
> connected. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: fediverse icon. Centre: "Social Web". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Social Web" in FOSDEM purple (#AF2C93).
> Connected-people icon.
> **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: fediverse instance map. Hand-drawn illustration, FOSDEM purple,
> dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Software Defined Radio(SDR)/Digital Signal Processing(DSP)

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "SDR/DSP". Stylised radio antenna emitting signal
> waves that transform into digital waveforms. FOSDEM purple, dark
> charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: radio spectrum waterfall display rendered as geometric
> colour blocks. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: antenna icon. Centre: "SDR / DSP". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "SDR" in FOSDEM purple (#AF2C93). Antenna
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: FFT spectrum analyser display. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Software Defined Storage

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Software Defined Storage". Stylised stack of
> virtual storage volumes with code defining their configuration.
> FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: abstract storage cluster with replication arrows.
> Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: disk-stack icon. Centre: "Software Defined
> Storage". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "SDS" in FOSDEM purple (#AF2C93). Storage
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: Ceph/distributed storage architecture. Hand-drawn illustration,
> FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Software Performance

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Software Performance". Stylised speedometer/
> gauge reaching high performance zone. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: flame graph / performance profile visualisation. Orange
> flame blocks, dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: speedometer icon. Centre: "Software
> Performance". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Perf" in FOSDEM purple (#AF2C93). Gauge
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: benchmark results chart with latency/throughput. Flat
> vector, FOSDEM purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Testing and Continuous Delivery

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Testing and Continuous Delivery". CI/CD pipeline
> diagram with test, build, deploy stages. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: horizontal pipeline with green checkmarks and deploy
> arrows. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: checkmark+rocket icon. Centre: "Testing &
> CD". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "CI/CD" in FOSDEM purple (#AF2C93). Pipeline
> arrow icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: CI/CD pipeline stages. Hand-drawn illustration, FOSDEM purple,
> dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Tool the Docs

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Tool the Docs". Stylised document with wrench
> and markdown formatting symbols. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: documentation pages being assembled by tooling robots.
> Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: doc+wrench icon. Centre: "Tool the Docs".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Docs" in FOSDEM purple (#AF2C93). Wrench
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: docs-as-code workflow. Hand-drawn illustration, FOSDEM purple,
> dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Translations

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Translations". Stylised speech bubbles in
> multiple languages with translation arrows between them. FOSDEM
> purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: word cloud in multiple scripts and alphabets with
> connecting lines. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: globe+speech icon. Centre: "Translations".
> Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "i18n" in FOSDEM purple (#AF2C93). Globe
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: translation memory interface. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Virtualization and Cloud Infrastructure

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Virtualization and Cloud Infrastructure".
> Stylised cloud with VM boxes inside and hypervisor layer beneath.
> FOSDEM purple, dark charcoal, hand-drawn ink-line illustration.
> **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: cloud architecture with VMs, containers, and
> networking. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: cloud+VM icon. Centre: "Virtualization &
> Cloud". Dark charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Cloud" in FOSDEM purple (#AF2C93). Cloud+VM
> icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: hypervisor architecture diagram. Hand-drawn illustration, FOSDEM
> purple, dark charcoal.
> **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

### Workshops

**Cover (poster)** — 1000 × 1500 px

> Vertical poster for "Workshops". Hands-on workbench with laptop,
> tools, and collaborative sticky notes. FOSDEM purple, dark charcoal,
> hand-drawn illustration. **Dimensions: 1000 × 1500 pixels. PNG.**

**Backdrop** — 1920 × 1080 px

> Wide backdrop: workshop classroom with multiple screens and people
> coding. Orange and white on dark charcoal. No text.
> **Dimensions: 1920 × 1080 pixels. PNG.**

**Banner** — 1000 × 185 px

> Horizontal banner. Left: toolbox icon. Centre: "Workshops". Dark
> charcoal, FOSDEM purple.
> **Dimensions: 1000 × 185 pixels. PNG.**

**Logo** — 800 × 310 px

> Clearlogo on **transparent background**. "Workshops" in FOSDEM purple (#AF2C93).
> Toolbox icon. **Dimensions: 800 × 310 pixels. PNG with transparency.**

**Thumb** — 960 × 540 px

> Landscape thumb: hands-on workshop scene. Hand-drawn illustration, FOSDEM purple,
> dark charcoal. **Dimensions: 960 × 540 pixels. PNG.**

______________________________________________________________________

## Summary

| Level              | Count | Images per item | Total images |
| ------------------ | ----- | --------------- | ------------ |
| Show (FOSDEM 2026) | 1     | 5               | 5            |
| Season (tracks)    | 72    | 5               | 360          |
| **Total**          |       |                 | **365**      |

### Naming Convention for Output Files

Following the spec's asset naming pattern:

**Show-level:** `fosdem-2026-<type>.<ext>` → copied as Jellyfin names (`poster.png`, `backdrop.png`, `banner.png`, `logo.png`, `thumb.png`)

**Season-level:** `fosdem-2026-<track-slug>-<type>.<ext>` → copied as Jellyfin names (`cover.png`, `backdrop.png`, `banner.png`, `logo.png`, `thumb.png`)
