import { Send, Copy, Check } from "lucide-react";
import TerminalCard from "./TerminalCard";
import { motion } from "framer-motion";
import { useState } from "react";

export default function OutreachTabs({ outputs, active, setActive }) {
  const [copied, setCopied] = useState(false);
  const platforms = ["EMAIL", "LINKEDIN", "WHATSAPP", "INSTAGRAM"];

  const handleCopy = () => {
    navigator.clipboard.writeText(outputs?.[active]);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <TerminalCard title="OUTREACH_STRATEGY" icon={Send}>
      <div className="flex border-b border-white/5 mb-6 overflow-x-auto no-scrollbar">
        {platforms.map(p => (
          <button
            key={p}
            onClick={() => setActive(p)}
            className={`px-6 py-4 text-[9px] font-mono tracking-widest transition-all relative whitespace-nowrap ${
              active === p ? "text-[#FF9D00]" : "text-white/20 hover:text-white/40"
            }`}
          >
            {p}
            {active === p && (
              <motion.div layoutId="tabUnderline" className="absolute bottom-0 left-0 right-0 h-[2px] bg-[#FF9D00]" />
            )}
          </button>
        ))}
      </div>

      <div className="relative group p-6 bg-black/40 border border-white/5 rounded-sm min-h-[250px]">
        <div className="absolute top-4 right-4 z-20">
          <button 
            onClick={handleCopy}
            className="p-3 bg-[#FF9D00] text-black rounded-sm hover:scale-110 active:scale-95 transition-all shadow-lg shadow-[#FF9D00]/20"
          >
            {copied ? <Check size={14} /> : <Copy size={14} />}
          </button>
        </div>

        <div className="font-mono text-[13px] text-white/60 leading-relaxed whitespace-pre-wrap">
          {outputs?.[active] || "Analyzing stream..."}
        </div>
      </div>
    </TerminalCard>
  );
}