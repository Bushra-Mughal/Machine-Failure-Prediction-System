# Design System Specification: Aether Intelligence

## 1. Overview & Creative North Star

The **Creative North Star** for this design system is **"The Predictive Ethereal."** 

In an industry often dominated by heavy, dark "command center" aesthetics, this system breaks the template by leaning into high-key, airy environments that prioritize mental clarity and precise action. We treat data not as a static burden, but as a living, breathing pulse. 

By leveraging **intentional asymmetry**—such as expansive white space balanced against dense, hyper-precise data modules—we move away from the "bootstrap" grid. Elements should feel like they are floating in a pressurized, clean-room environment. Overlapping frosted glass surfaces and a high-contrast typography scale create a "Digital Curator" effect: the interface doesn't just show data; it intelligently presents insights.

---

## 2. Colors & Surface Philosophy

The palette is rooted in a spectrum of "Atmospheric Neutrals" punctuated by high-energy functional accents.

### Color Roles
*   **Primary (#0058bc):** The "Electric Blue" pulse. Used for high-level navigation and primary action states.
*   **Secondary (#006e1c):** The "Cyber Lime" indicator. Reserved exclusively for "Healthy" machine states and successful ML predictions.
*   **Surface Hierarchy:**
    *   `surface`: The base canvas (#f8f9fa).
    *   `surface-container-low`: Used for large background sections to create subtle structural shifts (#f3f4f5).
    *   `surface-container-lowest`: The brightest white (#ffffff), used for the highest-level interactive cards.

### The "No-Line" Rule
Standard 1px solid borders are strictly prohibited for sectioning content. Boundaries must be defined through:
1.  **Background Shifts:** A `surface-container-low` sidebar sitting against a `surface` main content area.
2.  **Tonal Transitions:** Using the `surface-container` tiers to nest information.
3.  **The Glass & Gradient Rule:** Floating panels (like predictive modals) must use **Glassmorphism**. Apply `surface-container-lowest` at 60% opacity with a `backdrop-blur` of 20px. 

### Signature Textures
Main CTAs should utilize a subtle linear gradient from `primary` (#0058bc) to `primary-container` (#0070eb) at a 135-degree angle. This adds "visual soul" and prevents the interface from feeling medically sterile.

---

## 3. Typography: The Technical Editorial

The type system pairs the geometric, "engineered" look of **Space Grotesk** with the neutral, high-legibility of **Inter**.

*   **Display & Headline (Space Grotesk):** Used for data hero-numbers and section titles. The slightly quirkier terminal ends of Space Grotesk suggest a high-tech, custom-built machine interface. 
    *   *Usage:* `display-lg` (3.5rem) for critical failure probabilities.
*   **Title, Body, & Label (Inter):** Used for all functional UI, descriptions, and metadata. Inter provides the "authoritative" voice required for industrial reliability.
    *   *Usage:* `label-sm` (0.6875rem) in all-caps with 0.05rem letter-spacing for technical sensor tags.

---

## 4. Elevation & Depth: Tonal Layering

We avoid traditional "material" shadows in favor of **Tonal Layering**.

*   **The Layering Principle:** Depth is achieved by "stacking." 
    *   *Example:* Place a `surface-container-lowest` card on top of a `surface-container-low` section. The slight delta in brightness creates a natural lift without visual clutter.
*   **Ambient Shadows:** For floating elements (Modals, Popovers), use a "Whisper Shadow":
    *   `box-shadow: 0 20px 40px rgba(25, 28, 29, 0.04);` (using `on-surface` color at 4% opacity).
*   **The "Ghost Border":** If a container requires a boundary for accessibility (e.g., in high-glare industrial environments), use `outline-variant` at **15% opacity**. Never use 100% opaque borders.
*   **Precise Lines:** When lines are necessary (e.g., Sparklines or X/Y axes), use 0.5px or 1px widths using the `outline` token to maintain a "high-precision instrument" feel.

---

## 5. Components

### Buttons
*   **Primary:** Gradient-filled (`primary` to `primary-container`), `md` (0.75rem) corner radius. Use `on-primary` for text.
*   **Secondary/Ghost:** No fill, `Ghost Border` (15% `outline-variant`). On hover, transition to `surface-container-high`.

### Input Fields
*   **Styling:** Background of `surface-container-lowest`. No bottom border; instead, a 1px `Ghost Border` around the entire container.
*   **States:** On focus, the border transitions to 1px solid `primary` (#0058bc) with a 2px soft outer glow.

### Cards & Lists (The "Breathable" Rule)
*   **Forbid Dividers:** Do not use horizontal lines between list items. Use `3` (1rem) or `4` (1.4rem) spacing from the scale to separate rows.
*   **The "Machine Pulse" Card:** A `surface-container-lowest` card with a 4px left-accent border of `secondary` (#006e1c) to indicate an active, healthy machine state.

### High-Tech Functional Components
*   **Predictive Sparklines:** Use `primary` for historical data and a dashed `tertiary` (#006481) line for the predicted failure trajectory.
*   **Status Orbs:** Small 8px circles using `secondary` (Healthy) or `error` (Failure Imminent). Use a 4px `on-secondary-container` soft glow to make them appear "lit" from within.

---

## 6. Do's and Don'ts

### Do
*   **Do** use asymmetrical layouts (e.g., a wide 8-column data visualization next to a narrow 4-column insight panel).
*   **Do** use `Space Grotesk` for numbers. Industrial data should feel "engineered."
*   **Do** prioritize vertical whitespace. If a layout feels cramped, increase spacing to the next tier in the scale (e.g., move from `6` to `8`).

### Don'ts
*   **Don't** use pure black (#000000). Use `on-surface` (#191c1d) for text to maintain the soft, high-end feel.
*   **Don't** use standard 1px borders. Use background color shifts or the `Ghost Border` fallback.
*   **Don't** use heavy shadows. If you can clearly see the shadow, it’s too dark. It should feel like ambient occlusion, not a drop shadow.
*   **Don't** use "Cyber Lime" for anything other than positive machine health or "Go" actions. Overusing it dilutes its functional power.