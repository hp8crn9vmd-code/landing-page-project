// Motion Configuration
const MOTION_CONFIG = {
    // Animation durations (in milliseconds)
    durations: {
        fast: 150,
        normal: 300,
        slow: 500,
        verySlow: 1000
    },
    
    // Easing functions
    easings: {
        easeInOut: 'cubic-bezier(0.4, 0, 0.2, 1)',
        easeOut: 'cubic-bezier(0, 0, 0.2, 1)',
        easeIn: 'cubic-bezier(0.4, 0, 1, 1)',
        linear: 'linear'
    },
    
    // Scroll thresholds
    scroll: {
        offset: 100,
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    },
    
    // Performance settings
    performance: {
        maxConcurrentAnimations: 10,
        throttleScroll: true,
        debounceResize: true
    },
    
    // Accessibility
    accessibility: {
        respectReducedMotion: true,
        keyboardNavigation: true,
        focusManagement: true
    },
    
    // Feature flags
    features: {
        svgAnimations: true,
        scrollAnimations: true,
        hoverEffects: true,
        parallax: false, // Disabled for performance
        particles: false // Disabled for performance
    }
};

// Export for use in main.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = MOTION_CONFIG;
}
