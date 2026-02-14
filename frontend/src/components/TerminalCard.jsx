export default function TerminalCard({
  title,
  icon: Icon,
  children,
  color = "#FF9D00",
  className = ""
}) {
  return (
    <div
      className={`group relative bg-[#0A0A0F]/90 backdrop-blur-3xl 
      border border-white/10 hover:border-[#FF9D00]/30 transition-all
      rounded-md p-6 flex flex-col shadow-[0_0_40px_rgba(0,0,0,0.6)] ${className}`}
    >
      <div className="flex items-center justify-between mb-6">

        <div className="flex items-center gap-4">
          <div className="p-2.5 bg-white/5 rounded-sm">
            <Icon size={16} style={{ color }} />
          </div>

          <span className="font-mono text-[13px] uppercase tracking-[0.3em]" style={{ color }}>
            {title}
          </span>
        </div>

        <div className="flex gap-2 opacity-30">
          <div className="w-1.5 h-1.5 rounded-full bg-white" />
          <div className="w-1.5 h-1.5 rounded-full bg-white" />
        </div>
      </div>

      <div className="flex flex-col flex-1">
        {children}
      </div>

      <div
        className="absolute inset-0 rounded-md pointer-events-none opacity-0 group-hover:opacity-100 transition-all"
        style={{ boxShadow: `0 0 60px ${color}12 inset` }}
      />
    </div>
  );
}
