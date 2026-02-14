import TerminalCard from "./TerminalCard";
import { User } from "lucide-react";

export default function PersonaCard({ persona }) {
  return (
    <TerminalCard title="PERSONA_DOSSIER" icon={User} color="#00FFC2">
      <div className="flex justify-between items-start mb-8">
        <div>
          <h2 className="text-5xl font-orbitron text-white leading-tight uppercase">
            {persona?.name || "Target Unknown"}
          </h2>
          <p className="text-[#00FFC2] font-mono text-[10px] uppercase tracking-[0.2em] mt-1">
            {persona?.role || "Infiltrator"}
          </p>
        </div>
        <div className="px-4 py-1 border border-[#00FFC2] text-[#00FFC2] text-[9px] font-mono rounded-full uppercase">
          {persona?.seniority || "Classified"}
        </div>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
        <div className="p-4 bg-white/5 border border-white/5 rounded-sm">
          <p className="text-[7px] text-white/30 uppercase tracking-widest mb-2 font-mono">Industry</p>
          <p className="text-[11px] font-mono text-white/80">{persona?.industry}</p>
        </div>
        <div className="p-4 bg-white/5 border border-white/5 rounded-sm">
          <p className="text-[7px] text-white/30 uppercase tracking-widest mb-2 font-mono">Communication Tone</p>
          <p className="text-[11px] font-mono text-white/80">{persona?.tone}</p>
        </div>
        <div className="p-4 bg-white/5 border border-white/5 rounded-sm md:col-span-2">
          <p className="text-[7px] text-white/30 uppercase tracking-widest mb-2 font-mono">Strategic Style Hint</p>
          <p className="text-[11px] font-mono text-white/80 leading-relaxed">
            {persona?.style_hint}
          </p>
        </div>
      </div>

      <div className="flex flex-wrap gap-4 border-t border-white/5 pt-6">
        {persona?.interests?.map((tag, i) => (
          <span key={i} className="text-[9px] font-mono text-white/20 italic"># {tag}</span>
        ))}
      </div>
    </TerminalCard>
  );
}