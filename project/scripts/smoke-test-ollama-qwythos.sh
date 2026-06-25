#!/usr/bin/env sh
set -eu

MODEL="${OLLAMA_CHAT_MODEL:-hf.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF:Q4_K_M}"

echo "Running a public-safe Ollama smoke test with model: ${MODEL}"
ollama run "${MODEL}" "Reply in one sentence: ArchFlow provider check is running."
