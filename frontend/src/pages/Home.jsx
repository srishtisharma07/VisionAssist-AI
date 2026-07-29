import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="relative min-h-screen bg-slate-950 text-white overflow-hidden">

      <div className="absolute top-20 left-20 w-96 h-96 bg-cyan-500/20 blur-[140px] rounded-full"></div>
      <div className="absolute bottom-10 right-20 w-96 h-96 bg-blue-500/20 blur-[140px] rounded-full"></div>

      <section className="relative z-10 flex flex-col items-center justify-center text-center min-h-screen px-6">

        <p className="text-cyan-400 tracking-widest uppercase mb-3">
          Agentic AI Personal Assistant
        </p>

        <h1 className="text-6xl md:text-7xl font-black bg-gradient-to-r from-cyan-300 via-white to-cyan-500 bg-clip-text text-transparent">
          VisionAssist AI
        </h1>

        <p className="mt-6 max-w-3xl text-slate-300 text-xl leading-relaxed">
          Control your computer using
          <span className="text-cyan-400"> hand gestures</span>,
          <span className="text-cyan-400"> voice commands</span>,
          AI reasoning,
          OCR,
          PDF understanding
          and automation —
          all from one intelligent assistant.
        </p>

        <div className="mt-10">

          <Link
            to="/assistant"
            className="bg-cyan-500 hover:bg-cyan-400 hover:shadow-[0_0_30px_rgba(34,211,238,0.5)] transition-all duration-300 px-8 py-4 rounded-xl text-lg font-semibold"
          >
            Launch Assistant
          </Link>

        </div>

      </section>

      <section className="relative z-10 max-w-7xl mx-auto px-8 pb-20">

        <h2 className="text-3xl font-bold text-center mb-12">
          Powerful Features
        </h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

          <div className="group bg-white/5 backdrop-blur-lg rounded-3xl p-7 border border-slate-700 hover:border-cyan-400 hover:-translate-y-2 hover:shadow-[0_0_35px_rgba(34,211,238,0.25)] transition-all duration-300">
            <div className="text-5xl mb-5 group-hover:scale-110 transition-transform duration-300">🖐</div>
            <h3 className="text-xl font-bold mb-2">Gesture Control</h3>
            <p className="text-slate-400">
              Activate and control the assistant using intuitive hand gestures.
            </p>
          </div>

          <div className="group bg-white/5 backdrop-blur-lg rounded-3xl p-7 border border-slate-700 hover:border-cyan-400 hover:-translate-y-2 hover:shadow-[0_0_35px_rgba(34,211,238,0.25)] transition-all duration-300">
            <div className="text-5xl mb-5 group-hover:scale-110 transition-transform duration-300">🤖</div>
            <h3 className="text-xl font-bold mb-2">AI Assistant</h3>
            <p className="text-slate-400">
              Understands voice commands and intelligently performs tasks.
            </p>
          </div>

          <div className="group bg-white/5 backdrop-blur-lg rounded-3xl p-7 border border-slate-700 hover:border-cyan-400 hover:-translate-y-2 hover:shadow-[0_0_35px_rgba(34,211,238,0.25)] transition-all duration-300">
            <div className="text-5xl mb-5 group-hover:scale-110 transition-transform duration-300">📄</div>
            <h3 className="text-xl font-bold mb-2">PDF Assistant</h3>
            <p className="text-slate-400">
              Upload, analyse and interact with PDF documents effortlessly.
            </p>
          </div>

          <div className="group bg-white/5 backdrop-blur-lg rounded-3xl p-7 border border-slate-700 hover:border-cyan-400 hover:-translate-y-2 hover:shadow-[0_0_35px_rgba(34,211,238,0.25)] transition-all duration-300">
            <div className="text-5xl mb-5 group-hover:scale-110 transition-transform duration-300">👁</div>
            <h3 className="text-xl font-bold mb-2">OCR Vision</h3>
            <p className="text-slate-400">
              Read printed text directly through the camera using OCR.
            </p>
          </div>

        </div>

      </section>

    </div>
  );
}