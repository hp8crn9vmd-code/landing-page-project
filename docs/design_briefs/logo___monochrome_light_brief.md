# Design Brief: Logo - Monochrome Light

## Asset Name
Logo - Monochrome Light

## Purpose
This asset will be used on the main landing page to logo - monochrome light. 
It plays a critical role in establishing brand identity and driving user engagement through visual communication.

## Deliverables
- logo-monochrome-light.en.svg
- logo-monochrome-light.en@2x.svg
- logo-monochrome-light.ar.svg
- logo-monochrome-light.ar@2x.svg
- @2x PNG fallback for retina displays

## Technical Specs
| Specification | Requirement |
|---------------|-------------|
| Format(s) | SVG (primary), PNG (fallback) |
| Dimensions | min_height: 40px, width: variable |
| Aspect Ratio | same as full color logo |
| Max File Size | 81,920 bytes |
| Retina Required | Yes |
| Poster Required | No |

## Localization and RTL Notes
- **Arabic version requires complete RTL layout adaptation** (not simple mirroring)
- Text elements should be repositioned for natural Arabic reading flow
- UI elements in screenshots should be mirrored (navigation, buttons, etc.)
- Allow 25-33% extra horizontal space for Arabic text expansion
- Maintain same visual hierarchy and balance as English version

## Accessibility
- **Alt Text Key:** header_logo_alt or footer_logo_alt
- **WCAG Requirements:** Human-reviewed alt text required for all images
- **Video Accessibility:** Provide captions for any spoken content
- **Color Contrast:** Maintain minimum 4.5:1 contrast ratio for text elements

## Acceptance Criteria
1. Visual fidelity matches brand guidelines and provided references
2. All files under 81,920 bytes each
3. Filenames exactly match specifications (case-sensitive)
4. Color profiles: sRGB for web, proper transparency where specified

## Delivery
- **Owner Role:** design
- **Deadline:** 7 days from assignment
- **Handoff Package:** Final production files, source files (PSD/AI/Figma), VTT captions (if video), poster image, usage guidelines

## Notes
- Brand color tokens: primary #0066FF, secondary #FF6B6B
- Safe area: maintain 20% padding around logo edges
- Test on both light and dark backgrounds
