import { motion } from "framer-motion";

export default function GlowingButton({ children, onClick, active = false, className = "" }) {
  return (
    <motion.button
      whileHover={{ scale: 1.02, boxShadow: active ? "0 0 25px rgba(255,157,0,0.25)" : "" }}
      whileTap={{ scale: 0.98 }}
      onClick={onClick}
      className={`px-8 py-4 rounded-sm border font-orbitron tracking-[0.25em] text-[10px] uppercase flex items-center justify-center gap-3 transition-all ${
        active 
        ? "bg-[#FF9D00] text-black border-[#FF9D00]" 
        : "border-[#FF9D00]/40 text-[#FF9D00] hover:border-[#FF9D00] hover:bg-[#FF9D00]/5"
      } ${className}`}
    >
      {children}
    </motion.button>
  );
}