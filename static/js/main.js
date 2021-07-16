window.bufferToString = buffer => (
    String.fromCharCode.apply(null, new Uint8Array(buffer))
);

async function main() {
    await loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.17.0/full/"
    });

    const script = await fetch("/static/py/main.py");
    const scriptText = await script.text();
    pyodide.runPythonAsync(scriptText);
}

main();