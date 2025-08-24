# Project Kickstart Guide

## Project Metadata
**Instructions for User:** Fill in these fields when starting a new project. Leave blank fields if uncertain - Claude will ask follow-up questions.

**Project Name:** ADDevil - ADHD-Friendly Todo System  
**Primary Goal:** Design and prototype a todo system specifically for people with ADHD (inattentive type focus)  
**Key Challenge/Problem:** Traditional todo systems overwhelm ADHD brains - need system that works with ADHD patterns, not against them  
**Success Looks Like:** Working data model + basic visualization that demonstrates ADHD-specific features like Three-List System, overwhelm prevention  
**Timeline/Urgency:** Brainstorming/prototyping phase - no rush, focus on getting the concepts right  
**Estimated Complexity:** Medium - start simple with data model, expand to visualization/prototype 

**Instructions for Claude:** 
- Read this metadata section FIRST when starting any new project session
- If fields are complete, use this context to frame all conversations
- If fields are incomplete or blank, run a "project setup interview" with create-next-app style questions to gather missing information
- Reference this metadata throughout the project to maintain focus on stated goals

---

## Purpose
This file contains instructions for Claude on how to approach life project folders. Copy this to new project folders as `CLAUDE.md` to establish consistent working methodology.

## Project Philosophy
- **Action-oriented**: The ultimate goal is enabling real-world action, not endless planning
- **Iterative**: Build knowledge and insights over time through repeated conversations
- **Structured**: Use CLAUDE.md as persistent knowledge storage across sessions
- **Artifact-driven**: Create supporting tools/documents only when they genuinely help move thinking forward

## Working Approach
1. **Maintain Context**: Always update CLAUDE.md with key insights, decisions, and next steps
2. **Build on Previous Work**: Start each session by referencing what we've established before
3. **Focus on Unlocking**: Help identify and work through stuck points and hang-ups
4. **Balance Thinking and Action**: Connect abstract insights to concrete next steps
5. **Leverage Strengths**: Use my natural abilities while addressing limitations

## File Structure for Projects
- `CLAUDE.md`: Session notes, insights, decisions, next actions (project-specific)
- `Me.md`: Personal profile for context (shared file - see instructions below)
- Additional artifacts as needed: lists, templates, tools, analysis documents

## Personal Context Setup
**Important:** Do NOT copy Me.md to project folders. Instead, use the shared version:
- **Shared Me.md location:** `/Users/pjuele/Documents/Life/Me/Me.md`
- **Claude instruction:** Read the shared Me.md file from the above absolute path at the start of each session
- **If file not found:** Immediately notify the user that the Me.md file cannot be accessed at the expected location - do NOT proceed silently. Ask user to verify the file path or provide alternative location.

## Claude's Role
- Help structure thinking and identify patterns
- Provide outside perspective on blind spots
- Suggest frameworks and approaches
- Keep conversations focused on the project's ultimate real-world goals
- Generate artifacts only when they serve the larger purpose

## CRITICAL: Design & Styling Standards
**ALWAYS** refer to `/Users/pjuele/Documents/Life/styles/style-guidelines.md` for ALL UI/design work.

Key requirements:
- **Shadcn UI aesthetic** - minimal, professional, clean
- **Exact color palette**: #09090b (page), #181818 (panels), #252525 (elements), #404040 (hover)
- **Single text color**: #E5E5E5 throughout
- **Accent colors ONLY for borders** - never backgrounds
- **No rainbow interfaces** - stick to neutral grays with subtle accents

This is non-negotiable for maintaining consistency across all life projects.

## Session Flow
1. **Read shared Me.md** from `/Users/pjuele/Documents/Life/Me/Me.md` for personal context
2. **Read project metadata** at top of this file for project-specific context
3. Review previous CLAUDE.md to understand where we left off
4. Explore current challenges or questions
5. Develop insights and potential approaches
6. Identify concrete next steps
7. Update CLAUDE.md with key outcomes

---

## Session Notes & Progress

### Session 1 - Initial Brainstorming (Aug 23, 2025)

**Key ADHD Todo System Requirements Identified:**

From ADDitude Magazine research:
- **Three-List System**: Long List (everything), Routine List (timed/situational), Short List (daily focus)
- **Single-Item Focus**: Best solution is limiting to one item to prevent overwhelm
- **Priority Categories**: "Now," "Later," "Parking Lot" approach
- **Time Awareness**: ADHD brains overestimate available time - need realistic time booking
- **Master List Management**: Turn stagnant lists into daily action plans

**Completed Features:**
1. ✅ Design data model incorporating Three-List System
2. ✅ Add time estimation/booking features
3. ✅ Include overwhelm prevention mechanisms  
4. ✅ Consider routine/habit integration
5. ✅ Create visual wireframes with proper Shadcn UI styling
6. ✅ Build interactive prototype with drag-and-drop functionality
7. ✅ Implement responsive design for mobile/tablet
8. ✅ Add completion animations and visual feedback
9. ✅ Create reusable animation system
10. ✅ Build JSON-based project management with priority visualization
11. ✅ Fix UX bugs (blue frame persistence, focus limit feedback, rejected task feedback)
12. ✅ Add ADHD-friendly completion sound effects with Web Audio API

**Design System Established:**
- Implemented Shadcn UI color palette and design principles
- Created shared style guidelines at `/Users/pjuele/Documents/Life/styles/style-guidelines.md`
- Created reusable animations CSS at `/Users/pjuele/Documents/Life/styles/animations.css`
- Updated CLAUDE.md to enforce consistent styling across all future projects

**Current Project Status:**
- **prototype.html**: Fully functional ADHD-friendly todo system with Three-List System, drag-and-drop, focus mode, mobile responsiveness, completion animations, and Web Audio API sound effects
- **todos.html**: Project management visualization with active/completed task columns, priority-based sorting, and grayed-out completed tasks
- **todo.json**: 23 tracked project todos with metadata and status tracking (multiple tasks completed this session)
- **Style system**: Comprehensive guidelines and animation library for consistent design

**Session 2 - Header Design & Task Creation (Aug 24, 2025):**
- ✅ Comprehensive header redesign: responsive flexbox layout, logo integration, professional design
- ✅ Lucide Icons implementation with icon-only buttons and CSS tooltips
- ✅ Sound toggle functionality with proper icon state management (volume-2/volume-x)
- ✅ Task creation system: + button in Long List header with keyboard shortcut (+)
- ✅ Brain-dump mode: Enter saves task and keeps input open, ESC/click-outside closes
- ✅ ADHD-friendly defaults for new tasks: priority=now, energy=medium, duration=30min
- ✅ Priority-based task sorting in Long List (now → later → parking)
- ✅ Drag-drop completion with celebration sound and animation
- ✅ Expanded drag-drop areas: entire column clickable, not just blue dashed zones
- ✅ Break button functionality: paused overlay with break options menu
- ✅ 5-minute break timer with visual countdown, skip/extend options, auto-resume
- ✅ Proper ESC/click-outside navigation: timer→menu→focus mode hierarchy
- ✅ Fixed multiple timer interval bugs causing double-speed countdowns

**Break System Features:**
- Paused overlay with 4 break options: Timer, Breathing, Movement, Brain Dump
- 20-second test timer (configurable) with large countdown display
- Skip Break / +1 Min buttons for ADHD flexibility needs
- Proper navigation flow: ESC/click-outside goes back one level
- Auto-resume work after break completion with encouragement
- Clean timer interval management to prevent double-counting issues

**Files Updated This Session:**
- **prototype.html**: Major header redesign, task creation, break system, timer fixes
- **todo.json**: Updated completed tasks (#2, #6, #13, #22, #25) + new task #26 (visual timer)
- **todos.html**: Auto-refresh every 10 seconds with visual indicator

**Session 3 - Epic Tasks & Priority System Update (Aug 24, 2025):**
- ✅ Added "Epic" as largest duration option for complex multi-day projects
- ✅ Epic task visual styling: lighter background (#404040), bold white "😓 Epic" text with emoji
- ✅ Epic tasks retain priority border colors while adding distinctive appearance
- ✅ Expanded priority system: "now/later/parking" → "today/this week/later/parking"
- ✅ Updated priority colors: Today (red), This week (orange), Later (yellow), Parking (gray)
- ✅ Fixed CSS class generation for priorities with spaces ("this week" → "this-week")
- ✅ Updated sample tasks and defaults to use new priority system
- ✅ Completed all 4 break system options:
  - ⏰ **Timer**: 5-minute countdown with skip/extend options
  - 🚶 **Movement**: 12 randomized exercises with optional timers
  - 📝 **Brain Dump**: Persistent notepad with categorization
  - 🫁 **Breathing**: 4-7-8 technique with visual guide
- ✅ Created comprehensive README.md with user guide and technical documentation

**Epic Task System:**
- Visual distinction helps users identify tasks that need breakdown before focus
- 😓 emoji conveys appropriate ADHD overwhelm feeling for large tasks
- Maintains priority system while adding size indication
- User responsible for breaking down epics before dragging to focus (intentional design choice)

**Enhanced Priority System:**
- More nuanced time-based prioritization than previous system
- Clearer semantic meaning: today vs this week vs later vs parking
- Proper CSS class handling for multi-word priorities
- Maintains ADHD-friendly sorting and visual organization

**Session 4 - Layout & UI Improvements (Aug 24, 2025):**
- ✅ Moved focus mode button from bottom of Long List to top toolbar beside Lucide icons
- ✅ Added ENTER keyboard shortcut to start focus mode, ESC to exit focus mode  
- ✅ Implemented focus.jpg background image for focus mode with semi-transparent overlay
- ✅ Organized all assets into proper public/ directory structure (images/, favicons/)
- ✅ Created floating keyboard shortcuts legend in bottom-right corner
- ✅ Added contextual shortcuts that appear below task input box
- ✅ Fixed column layout system: removed equal height constraints, now content-based sizing
- ✅ Added empty state text for Routines column: "No routines set up yet ⏰ Add recurring habits here"
- ✅ Simplified Today's Focus title: made counter part of single text string to prevent line breaks

**Layout & UX Improvements:**
- **Focus button positioning**: Dual approach with icon in focus header + button in main toolbar
- **Keyboard shortcuts**: Comprehensive system with main legend + contextual input hints
- **Asset organization**: Professional file structure with public/images/ and public/favicons/
- **Responsive columns**: Content-based heights instead of forced equal sizing
- **Clean focus title**: Single string prevents flex layout issues and line breaks
- **Visual focus mode**: Atmospheric background image with proper overlay effects

**Session 5 - Project Organization & Index Creation (Aug 24, 2025):**
- ✅ Created organized folder structure: prototype/, analysis/, pm/
- ✅ Moved prototype.html to prototype/ folder with updated asset references
- ✅ Moved wireframes.html to analysis/ folder
- ✅ Moved todo.json and todos.html to pm/ folder
- ✅ Updated all asset paths in prototype.html to use ../public/ references
- ✅ Created professional index.html landing page with navigation cards
- ✅ Added server status indicator and project descriptions
- ✅ Updated README.md to reflect new project structure and server usage
- ✅ All links in index open in new tabs as requested

**Project Organization Improvements:**
- **Clean separation of concerns**: Prototype, analysis, and project management in dedicated folders
- **Professional file structure**: Follows web development best practices with public/ assets
- **Navigable index page**: Clean landing page using Shadcn UI design system
- **Updated documentation**: README reflects new structure and getting started process
- **Asset path consistency**: All references properly updated for new folder locations

**Session 6 - Git Repository & README Enhancement (Aug 24, 2025):**
- ✅ Set up git repository and resolved HTTP 400 push errors with buffer size fix
- ✅ Created and published addevil-v2 repository on GitHub
- ✅ Added project logo (devil.png) to README header with repo-hosted image
- ✅ Reorganized README structure: project logo + title, subtitle styling
- ✅ Created professional brand card footer with Shadcn UI styling
- ✅ Integrated personal branding (WDPJ logo) with proper attribution
- ✅ Fixed link structure so only logo and name are clickable, not "Built by"
- ✅ Applied consistent color scheme and professional card design

**Git & Documentation Improvements:**
- **Repository setup**: Professional GitHub presence with organized file structure
- **README enhancement**: Clean project branding with both project and personal logos
- **Brand integration**: Professional attribution card following design system
- **Technical resolution**: Solved git push issues with HTTP buffer configuration

**Communication Calibration:**
- Updated Me.md with critical feedback preferences for realistic professional validation
- Established collaborative approach: building on ideas rather than just cheerleading
- Focus on industry standards and constructive perspective for solo developer growth

**Ready for Next Session:**
Complete ADHD todo system with professional GitHub presence, comprehensive documentation, and established communication framework for effective collaboration. System ready for real-world testing or additional enhancements from backlog.

**IMPORTANT REMINDER:** When user says "update your admin files" - this includes both CLAUDE.md AND README.md updates.

---
*Copy this file to new project folders as CLAUDE.md to establish consistent working methodology.*