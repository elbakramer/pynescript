## Quick Start
- Library entry points live in `src/pynescript/ast/helper.py`; use `parse`, `dump`, and `unparse` to stay aligned with the public API.
- CLI mirrors helper flows (`parse-and-dump`, `parse-and-unparse`, `download-builtin-scripts`) in `src/pynescript/__main__.py`; automation should invoke those commands or their helper equivalents.
- Hatch environments drive tooling: `hatch run lint:style`, `hatch run lint:typing`, `hatch run test:test`, `hatch run docs:build`.

## Architecture
- Parsing runs through ANTLR grammars (`src/pynescript/ast/grammar/antlr4`) into the 1k-line `PinescriptASTBuilder` visiting parse trees into ASDL-generated nodes (`src/pynescript/ast/grammar/asdl/generated/PinescriptASTNode.py`).
- `StatementCollector` (`src/pynescript/ast/collector.py`) walks statements to align comment metadata; keep `annotations` lists intact when editing nodes or unparser output drifts.
- `NodeUnparser` (`src/pynescript/ast/unparser.py`) and `NodeLiteralEvaluator` (`src/pynescript/ast/evaluator.py`) assume canonical node shapes; manipulating ASTs should happen via `NodeTransformer` patterns.
- Comments tagged with `//@version`, `//@description`, etc. become annotation strings; `_add_annotations` in `helper.py` distributes them to script/function/type/variable nodes.

## Generated Assets
- Never hand-edit files in `src/pynescript/ast/grammar/**/generated`; regenerate grammars with `python src/pynescript/ast/grammar/antlr4/tool/generate.py` and ASDL nodes with `python src/pynescript/ast/grammar/asdl/tool/generate.py`.
- Regeneration copies helper stubs alongside grammar outputs; follow up with `hatch run lint:format` to enforce Ruff/Black expectations (120-column width, required future import).

## Testing & Fixtures
- Core regression: `pytest tests` (or the hatch alias) parses/unparses every `.pine` fixture in `tests/data/builtin_scripts`, comparing reprs for exact structural stability.
- Refresh fixtures with `pynescript download-builtin-scripts --script-dir tests/data/builtin_scripts`; this script hits TradingView's Pine facade via `src/pynescript/util/pine_facade.py` using `requests` + `tqdm`.
- `pytest --example-scripts-dir path/to/pine` lets you point at alternate corpora without editing fixtures.

## Conventions & Utilities
- Always place `from __future__ import annotations` first; Ruff's `required-imports` will fail otherwise.
- Generated AST nodes expose `_fields`/`_attributes`; traversal helpers (`iter_fields`, `iter_child_nodes`, `walk`) live in `ast/helper.py` and should be reused instead of manual attribute iteration.
- `NodeLiteralEvaluator` only covers deterministic literals and selected Pine built-ins; extend it cautiously with explicit validation.

## Integrations & Docs
- Pygments lexer adapter (`src/pynescript/ext/pygments/lexers.py`) maps ANTLR token ids to Pygments tokens; revise when grammar tokens change.
- Nautilus Trader stub (`src/pynescript/ext/nautilus_trader/strategy.py`) wires config hooks but leaves strategy logic empty—preserve method signatures.
- MyST docs under `docs/` pull live code via `{literalinclude}` from `examples/`; keep sample scripts executable when editing docs.
- `docs/pinescript_implementation_status.md` is the feature coverage ledger—update alongside grammar or evaluator enhancements.
