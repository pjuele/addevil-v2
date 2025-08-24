<div align="center">
  <img src="public/images/devil.png" alt="ADDevil Logo" width="80">
  
  # ADDevil
  *ADHD-Friendly Todo System*
</div>

A task management prototype specifically designed for people with ADHD, implementing evidence-based strategies from ADDitude Magazine and ADHD research to work with ADHD brains rather than against them.

## Development Approach

This project showcases a collaborative development methodology where I leveraged AI assistance while maintaining full technical leadership and vision control. Rather than traditional solo coding, I chose to test-drive modern AI tools by treating the AI as a capable junior developer - providing clear requirements, architectural guidance, and iterative feedback to achieve professional standards.

This approach allowed me to focus on my core strengths in analysis, product vision, and user experience while rapidly prototyping ideas. All technical decisions, UX choices, and quality standards remained under my direction, with the AI handling implementation details under supervision.

The project also includes a self-contained task management system (`pm/todo.json` and tracking interface) as an intentional alternative to external project management tools, keeping all project data within the repository and demonstrating portable project organization approaches.

The complete development process is documented in `CLAUDE.md` as a transparent case study in effective AI collaboration for professional development projects.

## 🧠 Why ADDevil?

Traditional todo apps overwhelm ADHD brains with endless lists and complex organization systems. ADDevil takes a different approach:

- **Three-List System**: Long List (everything), Today's Focus (max 3 tasks), Completed (dopamine hits)
- **Overwhelm Prevention**: Hard limits on focus tasks to prevent paralysis
- **Immediate Feedback**: Visual and audio cues for every action
- **Brain-Dump Friendly**: Quick task creation without friction
- **Break Integration**: Built-in movement, breathing, and mental breaks

## 🚀 Getting Started

1. Run `python server.py` from the project directory
2. Open http://localhost:8000 in your web browser
3. Choose your destination:
   - **Prototype**: Interactive ADHD todo system
   - **Analysis**: Design wireframes and research
   - **Project Management**: Development backlog
4. In the prototype, start with sample tasks or add your own
5. Drag tasks from Long List to Today's Focus (max 3)
6. Click the focus button to enter distraction-free work mode

## 📋 Core Features

### Three-List Task Management

**Long List**
- Your master task repository
- Priority levels: Today (urgent), This Week (important), Later (planned), Parking (someday)
- Add tasks with the + button or + keyboard shortcut
- Brain-dump mode: Enter to add and keep typing, ESC to close

**Today's Focus**
- Maximum 3 tasks to prevent overwhelm
- Drag tasks from Long List to add
- Visual feedback when trying to exceed the limit
- Click any task to edit details (duration, energy, priority)

**Completed**
- Celebration animations and sounds for dopamine boost
- Drag tasks here or mark complete in focus mode
- Visual history of your accomplishments

### Focus Mode

Enter deep work with a distraction-free interface:

- **25-minute Pomodoro timer** with visual countdown
- **Energy tracking** that decreases over time
- **Smart suggestions** based on your current state
- **Task switching** with ADHD-friendly warnings
- **Break system** with multiple options

### Break System

When you need a mental reset, choose from:

**⏰ Timed Break**
- 5-minute countdown timer (configurable to 20 seconds for testing)
- Skip early or add time as needed
- Auto-resume work when complete

**🚶 Movement Break**
- 12 randomized exercises from desk stretches to energy boosters
- Specific instructions: "10 desk push-ups" not "stretch a bit"
- Optional timers for each exercise
- "Next Exercise" button to find something that appeals

**📝 Brain Dump**
- Large text area for racing thoughts
- Auto-save as you type, persists between sessions
- Quick categorization: Ideas, Tasks, Shopping, Random
- Clear mental slate to return to focused work

**🫁 Breathing Exercise**
- 4-7-8 breathing technique with visual guide
- Animated circle with color-coded phases
- 4 automatic cycles for optimal calming effect
- Perfect for ADHD anxiety and overwhelm

### ADHD-Specific Features

**Overwhelm Prevention**
- Hard 3-task limit on focus list with friendly warnings
- Visual and audio feedback for rejected actions
- Priority-based task sorting to reduce decision fatigue

**Instant Gratification**
- Completion sounds and animations
- Visual progress tracking
- Immediate feedback for all interactions

**Flexibility**
- ESC key navigation throughout the system
- Click-outside to go back/close modals
- Skip options for every guided activity

**Sensory Features**
- Toggle sound system (completion chimes, focus tones, error sounds)
- Visual animations and state changes
- Tactile drag-and-drop interactions

## 🎮 User Guide

### Adding Tasks
1. Click the + button in the Long List header (or press +)
2. Type your task and press Enter to save and continue
3. Press ESC or click outside to close the input
4. New tasks default to: Priority=Now, Energy=Medium, Duration=30min

### Managing Tasks
- **Edit**: Click any task to open edit form with duration, energy, and priority options
- **Move**: Drag tasks between lists
- **Complete**: Drag to Completed column or use focus mode completion
- **Priority**: Edit tasks to set Now/Later/Parking priority (affects sort order)

### Focus Mode
1. Drag 1-3 tasks to Today's Focus
2. Click "Start Focus" button
3. Work on your task with the timer running
4. Use break button when needed
5. Complete task or switch when done

### Break Navigation
- **Break Menu**: ESC or click-outside returns to focus mode
- **Break Activities**: ESC or click-outside returns to break menu
- **Skip Options**: Available in all timed activities
- **Flexibility**: Every break can be shortened, extended, or skipped

### Keyboard Shortcuts
- **+**: Add new task to Long List
- **ESC**: Navigate back/close overlays throughout the system
- **Click outside**: Alternative to ESC for closing modals

## 🛠 Technical Details

### Project Structure
- **`index.html`**: Landing page with navigation to all sections
- **`prototype/`**: Interactive ADHD todo system prototype
- **`analysis/`**: Design wireframes and research documentation  
- **`pm/`**: Project management with backlog and completed features
- **`public/`**: Static assets (images, favicons, etc.)
- **`server.py`**: Simple HTTP server for local development

### Features
- **Local Storage**: Tasks and settings persist between sessions
- **Web Audio API**: For ADHD-friendly sound feedback
- **Responsive Design**: Works on desktop, tablet, and mobile
- **No dependencies**: Pure HTML, CSS, and JavaScript
- **File Organization**: Professional structure with separated concerns

## 🎯 ADHD Research Foundation

This system implements strategies from ADHD research including:

- **External brain** concept: Get tasks out of your head
- **Hyperfocus optimization**: Distraction-free environment with timer
- **Dopamine regulation**: Completion rewards and progress visualization
- **Executive function support**: Reduced decision making and clear next actions
- **Anxiety management**: Breathing exercises and overwhelm prevention
- **Movement integration**: Physical breaks to reset attention

## 📊 Project Status

Current prototype includes:
- ✅ Three-list task management system
- ✅ Drag-and-drop interface with ADHD-friendly feedback
- ✅ Focus mode with 25-minute Pomodoro timer
- ✅ Complete break system (timer, movement, brain dump, breathing)
- ✅ Task editing with duration/energy/priority options
- ✅ Sound system with user controls
- ✅ Mobile-responsive design
- ✅ LocalStorage persistence

Future enhancements tracked in `pm/todo.json`:
- Visual timer representation
- Keyboard shortcuts
- Routine/habit integration
- Time tracking and calibration features
- Export/import functionality

## 🤝 Contributing

This is a research prototype exploring ADHD-specific task management. The system prioritizes:

1. **User experience over features**: Every interaction should feel natural and supportive
2. **ADHD brain patterns**: Work with hyperfocus, distractibility, and overwhelm rather than against them
3. **Evidence-based design**: Features grounded in ADHD research and user testing
4. **Simplicity**: Avoid feature creep that could overwhelm the target users

---

*ADDevil: Because sometimes you need a little devil on your shoulder to keep you focused* 😈

---

<div align="center">
  <div style="
    display: inline-block;
    background: #181818;
    border: 1px solid #252525;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 32px 0;
  ">
    <div style="display: flex; align-items: center; gap: 12px;">
      <a href="https://pablojuele.com" style="text-decoration: none !important; color: #E5E5E5 !important;">
        <img src="https://res.cloudinary.com/wdpj/image/upload/c_scale,q_auto,w_50/v1636746639/web-design-pablo-juele/logos/wdpj-logo_ddlpop.jpg" alt="Web Design Pablo Juele Logo" width="40" style="border-radius: 4px;">
      </a>
      <div>
        <div style="font-weight: 600; font-size: 14px; color: #E5E5E5;">Built by</div>
        <a href="https://pablojuele.com" style="text-decoration: none !important; color: #E5E5E5 !important; font-size: 16px;">Web Design Pablo Juele</a>
      </div>
    </div>
  </div>
</div>