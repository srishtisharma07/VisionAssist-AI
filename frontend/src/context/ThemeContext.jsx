import { createContext, useContext, useEffect, useState } from "react";

const ThemeContext = createContext(null);

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(() => {
    return localStorage.getItem("visionassist-theme") || "dark";
  });

  useEffect(() => {
    const root = document.documentElement;

    root.classList.remove("dark-theme", "light-theme");
    root.classList.add(`${theme}-theme`);

    localStorage.setItem("visionassist-theme", theme);
  }, [theme]);

  function toggleTheme() {
    setTheme((current) =>
      current === "dark" ? "light" : "dark"
    );
  }

  return (
    <ThemeContext.Provider
      value={{ theme, setTheme, toggleTheme }}
    >
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  return useContext(ThemeContext);
}