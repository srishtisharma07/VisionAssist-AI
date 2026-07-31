import { useEffect, useState } from "react";
import {
  ArrowRight,
  Bot,
  Hand,
  FileText,
  Activity,
  Sparkles,
} from "lucide-react";

import { Link } from "react-router-dom";
import { getAssistantState } from "../services/api";

export default function Home() {
  const [state, setState] = useState({
    active: false,
    status: "INACTIVE",
    last_gesture: "",
    last_command: "",
    last_tool: "",
    last_response: "",
    conversation: [],
  });

  useEffect(() => {
    async function loadState() {
      const data = await getAssistantState();

      setState({
        active: data.active || false,
        status: data.status || "INACTIVE",
        last_gesture: data.last_gesture || "",
        last_command: data.last_command || "",
        last_tool: data.last_tool || "",
        last_response: data.last_response || "",
        conversation: data.conversation || [],
      });
    }

    loadState();

    const interval = setInterval(loadState, 1000);

    return () => clearInterval(interval);
  }, []);

  const features = [
    {
      icon: Hand,
      title: "Gesture Control",
      description:
        "Interact with the assistant using intuitive hand gestures.",
    },
    {
      icon: Bot,
      title: "Agentic AI",
      description:
        "Plan and execute computer tasks using intelligent AI orchestration.",
    },
    {
      icon: FileText,
      title: "PDF Assistant",
      description:
        "Upload and extract information from your documents.",
    },
    {
      icon: Activity,
      title: "Live Monitoring",
      description:
        "Track gestures, commands, tools and responses in real time.",
    },
  ];

  return (
    <div className="space-y-12">

      {/* Hero */}

      <section className="relative overflow-hidden rounded-[2rem] border border-[var(--border-color)] bg-[var(--panel-bg)] px-8 py-14 lg:px-14 lg:py-20">

        <div className="absolute -top-24 -right-24 w-72 h-72 rounded-full bg-[var(--accent)]/10 blur-3xl" />
        <div className="absolute -bottom-24 -left-24 w-72 h-72 rounded-full bg-[var(--accent)]/5 blur-3xl" />

        <div className="relative max-w-4xl">

          <div className="inline-flex items-center gap-2 rounded-full border border-[var(--border-color)] bg-[var(--panel-soft)] px-4 py-2">

            <Sparkles
              size={15}
              className="text-[var(--accent)]"
            />

            <span className="text-xs font-semibold uppercase tracking-[0.18em] text-[var(--text-muted)]">
              Agentic AI Personal Assistant
            </span>

          </div>

          <h2 className="mt-7 text-5xl md:text-6xl lg:text-7xl font-extrabold leading-[1.02] text-[var(--text-main)]">
            Control your computer
            <span className="block text-[var(--accent)]">
              without touching it.
            </span>
          </h2>

          <p className="mt-7 max-w-2xl text-base md:text-lg leading-8 text-[var(--text-muted)]">
            VisionAssist AI combines hand gestures, voice commands,
            computer vision and agentic AI to turn natural interaction
            into real computer actions.
          </p>

          <div className="mt-9 flex flex-wrap gap-4">

            <Link
              to="/assistant"
              className="inline-flex items-center gap-2 rounded-xl bg-[var(--accent)] px-6 py-3.5 font-semibold text-white transition hover:opacity-90"
            >
              Launch Assistant
              <ArrowRight size={18} />
            </Link>

            <Link
              to="/gestures"
              className="inline-flex items-center gap-2 rounded-xl border border-[var(--border-color)] bg-[var(--panel-soft)] px-6 py-3.5 font-semibold text-[var(--text-main)] transition hover:border-[var(--accent)]"
            >
              Explore Gestures
            </Link>

          </div>

        </div>

      </section>

      {/* Live Overview */}

      <section>

        <div className="mb-6">

          <p className="page-eyebrow">
            Live Overview
          </p>

          <h2 className="text-2xl font-bold text-[var(--text-main)] mt-1">
            Assistant at a glance
          </h2>

        </div>

        <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-5">

          <div className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6">

            <p className="text-sm text-[var(--text-muted)]">
              Assistant State
            </p>

            <p className="text-2xl font-bold text-[var(--accent)] mt-3">
              {state.status}
            </p>

          </div>

          <div className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6">

            <p className="text-sm text-[var(--text-muted)]">
              Current Gesture
            </p>

            <p className="text-2xl font-bold text-[var(--text-main)] mt-3 truncate">
              {state.last_gesture || "--"}
            </p>

          </div>

          <div className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6">

            <p className="text-sm text-[var(--text-muted)]">
              Last Tool
            </p>

            <p className="text-2xl font-bold text-[var(--text-main)] mt-3 truncate">
              {state.last_tool || "--"}
            </p>

          </div>

          <div className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6">

            <p className="text-sm text-[var(--text-muted)]">
              Conversations
            </p>

            <p className="text-2xl font-bold text-[var(--text-main)] mt-3">
              {state.conversation.length}
            </p>

          </div>

        </div>

      </section>

      {/* Features */}

      <section>

        <div className="mb-6">

          <p className="page-eyebrow">
            Core Capabilities
          </p>

          <h2 className="text-2xl font-bold text-[var(--text-main)] mt-1">
            Built for natural interaction
          </h2>

        </div>

        <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-5">

          {features.map((feature) => {

            const Icon = feature.icon;

            return (
              <div
                key={feature.title}
                className="group bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6 transition-all duration-300 hover:-translate-y-1 hover:border-[var(--accent)]"
              >

                <div className="w-11 h-11 rounded-xl bg-[var(--accent-soft)] flex items-center justify-center">

                  <Icon
                    size={22}
                    className="text-[var(--accent)]"
                  />

                </div>

                <h3 className="text-lg font-bold text-[var(--text-main)] mt-5">
                  {feature.title}
                </h3>

                <p className="text-sm leading-6 text-[var(--text-muted)] mt-2">
                  {feature.description}
                </p>

              </div>
            );

          })}

        </div>

      </section>

      {/* Latest Activity */}

      <section className="grid lg:grid-cols-2 gap-5">

        <div className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6">

          <p className="page-eyebrow">
            Latest Activity
          </p>

          <h2 className="text-xl font-bold text-[var(--text-main)] mt-1">
            Last command
          </h2>

          <div className="mt-5 bg-[var(--panel-soft)] border border-[var(--border-color)] rounded-2xl p-5">

            <p className="text-[var(--text-main)]">
              {state.last_command || "No command recorded yet."}
            </p>

            <p className="text-sm leading-6 text-[var(--text-muted)] mt-3">
              {state.last_response || "No assistant response yet."}
            </p>

          </div>

        </div>

        <div className="bg-[var(--panel-bg)] border border-[var(--border-color)] rounded-3xl p-6">

          <p className="page-eyebrow">
            Quick Actions
          </p>

          <div className="grid gap-3 mt-5">

            <Link
              to="/assistant"
              className="flex items-center justify-between rounded-2xl bg-[var(--panel-soft)] border border-[var(--border-color)] px-5 py-4 transition hover:border-[var(--accent)]"
            >
              <span className="font-semibold text-[var(--text-main)]">
                Open Assistant
              </span>

              <ArrowRight
                size={18}
                className="text-[var(--accent)]"
              />
            </Link>

            <Link
              to="/pdf"
              className="flex items-center justify-between rounded-2xl bg-[var(--panel-soft)] border border-[var(--border-color)] px-5 py-4 transition hover:border-[var(--accent)]"
            >
              <span className="font-semibold text-[var(--text-main)]">
                Open PDF Workspace
              </span>

              <ArrowRight
                size={18}
                className="text-[var(--accent)]"
              />
            </Link>

            <Link
              to="/settings"
              className="flex items-center justify-between rounded-2xl bg-[var(--panel-soft)] border border-[var(--border-color)] px-5 py-4 transition hover:border-[var(--accent)]"
            >
              <span className="font-semibold text-[var(--text-main)]">
                System Settings
              </span>

              <ArrowRight
                size={18}
                className="text-[var(--accent)]"
              />
            </Link>

          </div>

        </div>

      </section>

    </div>
  );
}