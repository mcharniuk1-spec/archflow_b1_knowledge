# OpenRouter Provider Comparison Status

Date: 2026-07-03T08:32:43.150278+00:00
Status: completed
Reason: openrouter_comparison_generated

## Boundary

- Provider path: OpenRouter.
- Route: `yushchenko.source_scope_gate`.
- Input kind: sanitized digest only.
- Raw private source sent: false.
- API keys are not written to public files.
- Model selection is role/node-based, not Epic-based.

## Details

```json
{
  "estimated_cost_usd": 0.007938124999999999,
  "model": "qwen/qwen3.6-plus",
  "selection_reason": "first_available_yushchenko_source_scope_execution_model",
  "usage": {
    "completion_tokens": 3866,
    "completion_tokens_details": {
      "audio_tokens": 0,
      "image_tokens": 0,
      "reasoning_tokens": 2662
    },
    "cost": 0.007938125,
    "cost_details": {
      "upstream_inference_completions_cost": 0.0075387,
      "upstream_inference_cost": 0.007938125,
      "upstream_inference_prompt_cost": 0.000399425
    },
    "is_byok": false,
    "prompt_tokens": 1229,
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cache_write_tokens": 0,
      "cached_tokens": 0,
      "video_tokens": 0
    },
    "total_tokens": 5095
  }
}
```
