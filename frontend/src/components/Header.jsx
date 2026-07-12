function Header() {
  return (
    <header className="bg-slate-800 border-b border-slate-700 shadow-lg">
      <div className="max-w-7xl mx-auto px-6 py-5 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-white">
            VisionAssist AI
          </h1>

          <p className="text-slate-400 mt-1">
            Gesture Controlled Agentic Personal Assistant
          </p>
        </div>

        <div className="bg-green-600 text-white px-4 py-2 rounded-lg font-semibold">
          Backend Connected
        </div>
      </div>
    </header>
  );
}

export default Header;