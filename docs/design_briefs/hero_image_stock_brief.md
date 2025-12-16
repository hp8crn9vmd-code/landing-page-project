# Design Brief: Hero Image (Stock)

## Asset Name
Hero Image (Stock)

## Purpose
This asset will be used on the main landing page to hero image. 
It plays a critical role in establishing brand identity and driving user engagement through visual communication.

## Deliverables
- hero-background.en.jpg
- hero-background.en@2x.jpg
- hero-background.ar.jpg
- hero-background.ar@2x.jpg
- JPEG fallback for older browsers

## Technical Specs
| Specification | Requirement |
|---------------|-------------|
| Format(s) | WebP (primary), JPEG (fallback) |
| Dimensions | 1920×1080px (16:9), 2560×1080px (21:9) |
| Aspect Ratio | 16:9, 21:9, 1:1 |
| Max File Size | 256,000 bytes |
| Retina Required | Yes |
| Poster Required | No |

## Localization and RTL Notes
- No RTL mirroring required for this asset
- Arabic version should use the same composition as English
- For videos: provide Arabic captions/subtitles (VTT format)

## Accessibility
- **Alt Text Key:** hero_background_alt
- **WCAG Requirements:** Human-reviewed alt text required for all images
- **Video Accessibility:** Provide captions for any spoken content
- **Color Contrast:** Maintain minimum 4.5:1 contrast ratio for text elements

## Acceptance Criteria
1. Visual fidelity matches brand guidelines and provided references
2. All files under 256,000 bytes each
3. Filenames exactly match specifications (case-sensitive)
4. Color profiles: sRGB for web, proper transparency where specified

## Delivery
- **Owner Role:** design
- **Deadline:** 7 days from assignment
- **Handoff Package:** Final production files, source files (PSD/AI/Figma), VTT captions (if video), poster image, usage guidelines

## Notes
- Abstract gradient with geometric overlays only
- No human faces or identifiable text
- Multiple aspect ratios required: 16:9, 21:9, 1:1
