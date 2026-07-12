import { useState } from "react";
import { uploadPDF } from "../services/api";

function PDFUploadPanel() {

    const [selectedFile, setSelectedFile] = useState(null);
    const [status, setStatus] = useState("");

    async function handleUpload() {

        if (!selectedFile) {
            setStatus("Please select a PDF.");
            return;
        }

        setStatus("Uploading PDF...");

        const result = await uploadPDF(selectedFile);

        console.log(result);

        if (result.success === false) {
            setStatus(result.message);
            return;
        }

        if (result.message) {
            setStatus(result.message);
        } else {
            setStatus("Upload completed.");
        }
    }

    return (

        <div className="bg-slate-800 rounded-xl shadow-lg p-5">

            <h2 className="text-xl font-semibold text-white mb-5">
                📄 Upload PDF
            </h2>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) => setSelectedFile(e.target.files[0])}
                className="block w-full text-white mb-5"
            />

            <button
                onClick={handleUpload}
                className="w-full bg-green-600 hover:bg-green-700 text-white py-3 rounded-lg font-semibold"
            >
                Upload PDF
            </button>

            {selectedFile && (
                <p className="mt-4 text-slate-300">
                    Selected: {selectedFile.name}
                </p>
            )}

            {status && (
                <p className="mt-4 text-green-400">
                    {status}
                </p>
            )}

        </div>

    );
}

export default PDFUploadPanel;