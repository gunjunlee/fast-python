
use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn r_calc(x: i32) -> PyResult<f32> {
    let mut val = 1.;
    for i in 1..x {
        let i = i as f32;
        val += (1. / i).exp();
    }
    Ok(val)
}

#[pyfunction]
fn r_ng_calc(py: Python, x: i32) -> PyResult<f32> {
    let val = py.allow_threads(|| {
        let mut val = 1.;
        for i in 1..x {
            let i = i as f32;
            val += (1. / i).exp();
        }
        val
    });
    Ok(val)
}

/// A Python module implemented in Rust.
#[pymodule]
fn rfast(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(r_calc, m)?)?;
    m.add_function(wrap_pyfunction!(r_ng_calc, m)?)?;
    Ok(())
}
