import GlowingButton from "./GlowingButton";
import { Lock, Globe } from "lucide-react";

export default function LandingHero({ onEnter }) {
  return (
    <section className="relative flex-1 flex items-center justify-center overflow-hidden">

      <div className="absolute inset-0 pointer-events-none">
        <div className="absolute top-[40%] left-1/2 -translate-x-1/2 w-[900px] h-[900px] bg-[#FF9D00]/5 blur-[180px] rounded-full" />
      </div>

      <div className="relative z-10 max-w-[1200px] mx-auto px-6 text-center">
        <h1 className="text-7xl md:text-[9rem] font-black font-orbitron tracking-tight leading-none yugen-cursor">
          <span className="text-[#FF9D00]">YUGEN</span>AI
        </h1>

        <p className="mt-8 font-mono text-[#00FFC2] tracking-[0.35em] text-[14px] uppercase">
          STRATEGIC LOCAL INTELLIGENCE ENGINE
        </p>

        <div className="mt-14 flex flex-col md:flex-row gap-6 justify-center">
          <GlowingButton active onClick={onEnter}>
            <Lock size={14}/> ENTER TERMINAL
          </GlowingButton>

          <GlowingButton onClick={() => window.open('https://github.com/osinsomkuwar-27/YugenAI')}>
            <Globe size={14}/> REPO ACCESS
          </GlowingButton>
        </div>
      </div>
    </section>
  );
}
