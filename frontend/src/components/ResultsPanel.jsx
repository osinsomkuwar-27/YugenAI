import TerminalCard from "./TerminalCard";

export default function ResultsPanel({ results }) {

  if(!results){
    return (
      <div className="border border-dashed border-white/10 p-10 text-center text-white/20">
        Awaiting Intel Generation...
      </div>
    );
  }

  return (
    <>
      <TerminalCard title="PERSONA_DOSSIER">
        <pre>{JSON.stringify(results.persona,null,2)}</pre>
      </TerminalCard>

      <TerminalCard title="OUTREACH_STRATEGY">
        <pre>{results.outputs?.EMAIL}</pre>
      </TerminalCard>
    </>
  );
}
