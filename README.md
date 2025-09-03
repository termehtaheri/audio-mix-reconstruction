# audio-mix-reconstruction

**Reconstruct master mixes from stems** using **ridge regression**.  
Reports R², MSE, and per-stem gains, with optional error WAV export.  

> No proprietary data. Includes tiny synthetic stems for a quick demo.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -U pip && pip install -r requirements.txt
pip install -e .

# (optional) create tiny demo stems
python scripts/make_demo_stems.py  # writes stems + master to data/samples

# run reconstruction
python -m lmm.cli \
  --mode reconstruct \
  --master data/samples/master.wav \
  --stems_dir data/samples/stems \
  --report lmm_report.json
```

## Outputs
- `lmm_report.json`: sample_rate, alpha, R², MSE, per-stem gains  
- `error.wav` (optional): residual (master − reconstruction)

## Why this works
We model the master as a **linear combination of stems**. Ridge regression fits the optimal gains and reports reconstruction quality.

## Roadmap
- Group detection via R² thresholding  
- Spectral features for grouping  
- Alternative regressors (Lasso, ElasticNet)

## License
- Code: MIT (see `LICENSE`)
