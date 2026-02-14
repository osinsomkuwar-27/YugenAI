import { LogOut, Sparkles } from "lucide-react";

export default function Navbar({ uid = "TfHw8hCIcJ09...", onExit }) {
  return (
    <nav className="sticky top-0 z-20 w-full">
      <div className="max-w-[1600px] mx-auto px-8 py-4 flex justify-between items-center
        border-b border-white/5 backdrop-blur-sm bg-black/10">

        {/* LEFT */}
        <div className="flex items-center gap-4">
          <div className="w-9 h-9 bg-[#FF9D00] text-black font-black flex items-center justify-center rounded-sm text-lg font-orbitron">
            Y
          </div>

          <div className="leading-tight">
            <p className="font-orbitron text-[10px] tracking-widest text-[#FF9D00]">
              S-RANK ACCESS
            </p>
            <p className="font-mono text-[8px] text-white/30 uppercase tracking-tight">
              UID: {uid}
            </p>
          </div>
        </div>

        {/* RIGHT */}
        <div className="flex gap-5 items-center">
          <Sparkles size={16} className="text-white/20" />

          <button
            onClick={onExit}
            className="px-3 py-2 border border-red-500/20 text-red-500/70 hover:bg-red-500/10 transition-all font-mono text-[9px] uppercase tracking-widest flex items-center gap-2"
          >
            <LogOut size={12} /> TERMINATE
          </button>
        </div>
      </div>
    </nav>
  );
}
