import React, { useState } from 'react';
import Navbar from './components/Navbar';
import LandingHero from './components/LandingHero';
import TerminalCard from './components/TerminalCard';
import GlowingButton from './components/GlowingButton';
import PersonaCard from './components/PersonaCard';
import OutreachTabs from './components/OutreachTabs';
import { Terminal, Zap, RotateCcw } from 'lucide-react';

export default function App() {

  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [profileData, setProfileData] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);
  const [results, setResults] = useState(null);
  const [activeTab, setActiveTab] = useState("EMAIL");

  const executeGeneration = async () => {
    if (!profileData) return;

    setIsGenerating(true);
    setResults(null);

    try {
      const response = await fetch('http://localhost:8000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ profile: profileData })
      });

      const data = await response.json();
      setResults(data);
    } catch (err) {
      console.error("YugenAI Intel Error:", err);
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#050505] text-white overflow-x-hidden">

      {/* ===== LANDING ===== */}
      {!isLoggedIn ? (
        <div className="flex flex-col min-h-screen">
          <Navbar onExit={() => setIsLoggedIn(false)} />
          <LandingHero onEnter={() => setIsLoggedIn(true)} />
        </div>
      ) : (

        <div className="flex flex-col min-h-screen">
          <Navbar onExit={() => setIsLoggedIn(false)} />

          {/* ===== MAIN DASHBOARD ===== */}
          <main className="flex-1 max-w-[1700px] mx-auto w-full px-10 py-10">

            {/* ⭐ FLEX ROW = SIDE BY SIDE GUARANTEED */}
            <div className="flex flex-col lg:flex-row gap-8 w-full">

              {/* ================= LEFT PANEL ================= */}
              <div className="flex-1">
                <TerminalCard
                  title="INTEL_INPUT"
                  icon={Terminal}
                  className="h-[720px] flex flex-col"
                >
                  <textarea
                    value={profileData}
                    onChange={(e) => setProfileData(e.target.value)}
                    className="flex-1 w-full bg-transparent border-none focus:ring-0 
                    font-mono text-[18px] text-[#E6E6E6] leading-relaxed resize-none 
                    placeholder:text-white/30 caret-[#FF9D00]"
                    placeholder="PASTE LINKEDIN PROFILE OR LEAD DATA..."
                  />

                  <div className="mt-6 flex gap-4">
                    <GlowingButton
                      active
                      className="flex-1 text-[15px]"
                      onClick={executeGeneration}
                    >
                      {isGenerating
                        ? "EXTRACTING..."
                        : <><Zap size={18}/> GENERATE INTELLIGENCE</>}
                    </GlowingButton>

                    <button
                      onClick={() => { setProfileData(""); setResults(null); }}
                      className="p-5 border border-white/10 rounded-sm hover:bg-white/5 transition-all text-white/70"
                    >
                      <RotateCcw size={18} />
                    </button>
                  </div>

                </TerminalCard>
              </div>

              {/* ================= RIGHT PANEL ================= */}
              <div className="flex-1 flex flex-col gap-8">

                {results ? (
                  <>
                    <PersonaCard persona={results.persona} />

                    <OutreachTabs
                      active={activeTab}
                      setActive={setActiveTab}
                      outputs={results.outputs}
                    />
                  </>
                ) : (
                  <div className="h-[720px] border border-dashed border-white/10 rounded-lg flex flex-col items-center justify-center opacity-40">
                    <Terminal size={50} className="mb-6 animate-pulse" />
                    <p className="font-orbitron text-[16px] tracking-[0.25em] uppercase">
                      Awaiting Neural Link...
                    </p>
                  </div>
                )}

              </div>

            </div>

          </main>
        </div>
      )}
    </div>
  );
}
