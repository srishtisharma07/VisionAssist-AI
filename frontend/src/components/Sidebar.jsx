import { NavLink } from "react-router-dom";

function Sidebar() {
  const menu = [
    { name: "Home", path: "/" },
    { name: "Assistant", path: "/assistant" },
    { name: "Gesture Guide", path: "/gestures" },
    { name: "PDF Assistant", path: "/pdf" },
    { name: "Settings", path: "/settings" },
  ];

  return (
    <aside className="w-64 h-screen bg-slate-950 border-r border-slate-800 p-6">

      <h1 className="text-2xl font-bold text-white mb-10">
        VisionAssist AI
      </h1>

      <nav className="space-y-2">
        {menu.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `block px-4 py-3 rounded-lg transition ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-slate-300 hover:bg-slate-800"
              }`
            }
          >
            {item.name}
          </NavLink>
        ))}
      </nav>

    </aside>
  );
}

export default Sidebar;