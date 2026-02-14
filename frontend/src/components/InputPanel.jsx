import TerminalCard from "./TerminalCard";
import GlowingButton from "./GlowingButton";

export default function InputPanel({ profileData, setProfileData, executeGeneration, loading }) {
  return (
    <TerminalCard title="INTEL_INPUT">
      <textarea
        value={profileData}
        onChange={(e)=>setProfileData(e.target.value)}
        className="w-full min-h-[300px] bg-transparent text-white font-mono"
      />
      <div className="mt-4">
        <GlowingButton onClick={executeGeneration} loading={loading}>
          Generate Intelligence
        </GlowingButton>
      </div>
    </TerminalCard>
  );
}
