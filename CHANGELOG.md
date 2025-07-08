# Studibudi Changelog

## 0.0.2 — 8 Jul 2025
### What’s new ✨
- Hotjar tracking for in-app experience insights  
- Full service client replacing direct backend calls with cleaner APIs  
- Session auto-end and tidy-up logic keeps things snappy next time you study  
- 95 % migration from Supabase to dedicated service layer  
- Polished Agent Controls & Conversation Transcript components  
- Smarter data-fetch flow and steadier error handling on Document and Session pages  
- Built-in request de-duplication stops the “loop-storm” when network blips  
- Robust sidebar guard eliminates the dreaded white-page freeze  
- Unified **useSessionOrDocument** hook keeps context tight across the app  
- Credit tracker counts tokens in real time; usage is always crystal-clear  
- Friendly out-of-credits modal with one-tap top-up  
- Continuous logging: richer details if something ever misbehaves  
- Handy hamburger menu to show/hide the sidebar on smaller screens  
- New document button plus neat gutter spacing for a cleaner workspace  

### Improvements 🚀
- Local dev: standardised real-time WebSocket URL (`ws://localhost:8765`)  
- Faster local testing with single host for all service calls (`localhost:8080/service`)  
- Longer silence window (→ 1000 ms) prevents the AI from cutting you off mid-sentence  
- Fallback ports safeguard live sessions if 8080 is busy  
- Better time tracking: precise session length calculation every time  

### Fixes 🔧
- Sidebar width no longer jumps on reload  
- Removed stray `ApiCallMonitor` import that broke hot-reload  
- Replaced mock upload with real backend integration—no more phantom files  
- Long document names now truncate elegantly instead of breaking the layout  
- Fixed session-duration update race-condition  
- Mobile login spacing is finally pixel-perfect  
- New document button links to the right route every single time  
- Dark-mode quote animation renders smoothly on lower-end devices  

### Performance ⚡
- HTTP health-check endpoint keeps Cloud Run deployments humming under heavy load  

---

## 0.0.1 — 1 Jul 2025  
*(first public preview — hundreds of commits condensed below)*  

### What’s new ✨
- “Talk to Your PDF” – voice-query any page and hear context-aware answers  
- Live document switching inside one conversation  
- Instant resume: pick up exactly where you left off after a break  
- Dark-mode (early) plus brand-new Lexend font for easier reading  
- Secure login & signup with email verification and password reset  
- Full JWT-based auth under the hood (keeps your data safe)  
- Welcome quotes carousel for a warmer first impression  
- Fresh Studibudi logo and app icon across all platforms  
- Dynamic instruction engine (multi-layer context for smarter replies)  
- Session auto-end timer avoids runaway credit drain  
- Credit dashboard shows usage in real time  
- Live collaboration (beta): watch a study partner scroll in real time  
- Document deletion & “New Document” sidebar button  
- Forgot-password flow plus confirmation e-mails  
- Truncated long file names in the sidebar with hover-to-reveal  
- Inline PDF viewer: smooth zoom/pan without CORS hiccups  
- Background blur and quote animation on the login screen  
- Embedded health-check server for production monitoring  
- Animated loading spinner during large PDF uploads  
- Smart speech-interruption handling—no more “talking over” you  
- Mobile-first layout tweaks for phones and tablets  

### Improvements 🚀
- Massive style pass: unified buttons, dialogs, form inputs, and alerts  
- Better spacing on login & signup forms, clearer error messages  
- Consistent dark-mode colour palette and higher-contrast text  
- Sidebar alignment fixes when collapsed  
- Faster context loading at session start (~30 % quicker)  
- Document upload moved to multi-part streaming for big files  
- Cleaner footer layout and responsive grid in the dashboard  
- Button borders & hover states for stronger visual feedback  
- Input placeholders & outlines to guide first-time users  
- Quote component now runs a subtle fade animation instead of instant swap  
- Smarter silence detection during voice chat  
- Front-end environment switched to production build pipeline  
- Hardened auth persistence—no more surprise sign-outs  
- Removed dead code paths and legacy test assets  

### Fixes 🔧
- Re-enabled authentication check that occasionally let sessions start unauthenticated  
- Patched white-screen crash on network timeout  
- Closed rare infinite-loading loop in the PDF viewer  
- Eliminated duplicated session records in history tab  
- Corrected RAG embedding dimensional mismatch causing blank answers  
- Addressed CORS errors when loading large PDFs from certain domains  
- Fixed pagination bug in document list (last page sometimes empty)  
- Squashed sound-loop glitch when microphone briefly disconnects  
- Resolved “ghost” quote appearing twice on login page  
- Prevented accidental logout when browser cache is cleared  
- Fixed clipboard shortcut conflicts on Windows keyboards  
- Adjusted long-division rendering in math examples for Layla’s lessons  
- Countless minor typo clean-ups, null-pointer guards, and micro-perf tweaks  

---