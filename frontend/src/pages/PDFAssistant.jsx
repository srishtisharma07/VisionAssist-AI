import { useEffect, useRef, useState } from "react";
import {
    Upload,
    FileText,
    Trash2,
    X,
    CheckCircle2,
} from "lucide-react";

import {
    uploadPDF,
    getPdfInfo,
    getPdfText,
    deletePdf,
    clearAllPdfs,
} from "../services/api";

export default function PDFAssistant() {

    const fileInputRef = useRef(null);

    const [selectedFile, setSelectedFile] = useState(null);
    const [pdfInfo, setPdfInfo] = useState({
        total_pdfs: 0,
        uploaded_pdfs: [],
        characters: 0,
    });

    const [pdfText, setPdfText] = useState("");
    const [status, setStatus] = useState("");
    const [uploading, setUploading] = useState(false);

    async function refreshPdfData() {

        const info = await getPdfInfo();
        const text = await getPdfText();

        setPdfInfo(info);
        setPdfText(text.text || "");
    }

    useEffect(() => {
        refreshPdfData();
    }, []);

    function handleFileSelect(file) {

        if (!file) {
            return;
        }

        if (file.type !== "application/pdf") {
            setStatus("Please select a PDF file.");
            return;
        }

        setSelectedFile(file);
        setStatus("");
    }

    function handleDrop(event) {

        event.preventDefault();

        const file = event.dataTransfer.files[0];

        handleFileSelect(file);
    }

    async function handleUpload() {

        if (!selectedFile) {
            setStatus("Please select a PDF first.");
            return;
        }

        setUploading(true);
        setStatus("Uploading and processing PDF...");

        const result = await uploadPDF(selectedFile);

        if (result.success === false) {
            setStatus(result.message || "Upload failed.");
            setUploading(false);
            return;
        }

        setStatus(
            `✓ ${result.file_name || selectedFile.name} uploaded successfully.`
        );

        setSelectedFile(null);
        setUploading(false);

        await refreshPdfData();
    }

    async function handleDelete(filename) {

        const result = await deletePdf(filename);

        if (result.success === false) {
            setStatus(result.message || "Unable to delete PDF.");
            return;
        }

        setStatus(`${filename} removed.`);

        await refreshPdfData();
    }

    async function handleClearAll() {

        const result = await clearAllPdfs();

        if (result.success === false) {
            setStatus(result.message || "Unable to clear PDFs.");
            return;
        }

        setStatus("All PDFs removed.");

        await refreshPdfData();
    }

    return (

        <div className="space-y-8">

            {/* Header */}

            <div>

                <h1 className="text-4xl font-bold text-white">
                    PDF Assistant
                </h1>

                <p className="text-slate-400 mt-2">
                    Upload documents and prepare them for AI-powered analysis.
                </p>

            </div>

            {/* Upload + Info */}

            <div className="grid lg:grid-cols-3 gap-6">

                {/* Upload Area */}

                <div className="lg:col-span-2">

                    <div
                        onDragOver={(event) => event.preventDefault()}
                        onDrop={handleDrop}
                        className="bg-slate-900 border border-dashed border-slate-600 hover:border-cyan-400 rounded-3xl p-10 transition"
                    >

                        <div className="flex flex-col items-center justify-center text-center min-h-[320px]">

                            <div className="w-20 h-20 rounded-2xl bg-cyan-500/10 border border-cyan-400/30 flex items-center justify-center">
                                <Upload
                                    size={34}
                                    className="text-cyan-400"
                                />
                            </div>

                            <h2 className="text-2xl font-bold text-white mt-6">
                                Upload a PDF
                            </h2>

                            <p className="text-slate-400 mt-3 max-w-md">
                                Drag and drop your document here or browse your
                                computer to upload a PDF.
                            </p>

                            <button
                                onClick={() => fileInputRef.current?.click()}
                                className="mt-7 bg-cyan-500 hover:bg-cyan-400 text-white px-6 py-3 rounded-xl font-semibold transition"
                            >
                                Choose PDF
                            </button>

                            <input
                                ref={fileInputRef}
                                type="file"
                                accept=".pdf,application/pdf"
                                className="hidden"
                                onChange={(event) =>
                                    handleFileSelect(event.target.files[0])
                                }
                            />

                            {selectedFile && (

                                <div className="mt-6 w-full max-w-md bg-slate-800 rounded-2xl p-4 flex items-center justify-between">

                                    <div className="flex items-center gap-3 min-w-0">

                                        <FileText
                                            className="text-cyan-400 shrink-0"
                                            size={24}
                                        />

                                        <span className="text-white truncate">
                                            {selectedFile.name}
                                        </span>

                                    </div>

                                    <button
                                        onClick={() => setSelectedFile(null)}
                                        className="text-slate-400 hover:text-white"
                                    >
                                        <X size={20} />
                                    </button>

                                </div>

                            )}

                            <button
                                onClick={handleUpload}
                                disabled={!selectedFile || uploading}
                                className="mt-4 bg-green-600 hover:bg-green-500 disabled:bg-slate-700 disabled:text-slate-500 text-white px-6 py-3 rounded-xl font-semibold transition"
                            >
                                {uploading ? "Processing..." : "Upload & Process"}
                            </button>

                            {status && (

                                <p className="mt-5 text-sm text-cyan-300">
                                    {status}
                                </p>

                            )}

                        </div>

                    </div>

                </div>

                {/* Document Stats */}

                <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

                    <h2 className="text-xl font-bold text-white">
                        Document Library
                    </h2>

                    <div className="mt-6 space-y-5">

                        <div className="bg-slate-800 rounded-2xl p-5">
                            <p className="text-slate-400 text-sm">
                                Uploaded PDFs
                            </p>

                            <p className="text-3xl font-bold text-cyan-400 mt-2">
                                {pdfInfo.total_pdfs}
                            </p>
                        </div>

                        <div className="bg-slate-800 rounded-2xl p-5">
                            <p className="text-slate-400 text-sm">
                                Extracted Characters
                            </p>

                            <p className="text-3xl font-bold text-green-400 mt-2">
                                {pdfInfo.characters.toLocaleString()}
                            </p>
                        </div>

                        <button
                            onClick={handleClearAll}
                            disabled={pdfInfo.total_pdfs === 0}
                            className="w-full bg-red-500/10 border border-red-500/30 text-red-400 hover:bg-red-500/20 disabled:opacity-40 rounded-xl py-3 transition"
                        >
                            Clear All PDFs
                        </button>

                    </div>

                </div>

            </div>

            {/* Uploaded Documents */}

            <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

                <div className="flex items-center justify-between mb-6">

                    <h2 className="text-2xl font-bold text-white">
                        Uploaded Documents
                    </h2>

                </div>

                {pdfInfo.uploaded_pdfs.length === 0 ? (

                    <div className="text-center py-14 text-slate-500">
                        No PDFs uploaded yet.
                    </div>

                ) : (

                    <div className="space-y-3">

                        {pdfInfo.uploaded_pdfs.map((filename) => (

                            <div
                                key={filename}
                                className="flex items-center justify-between bg-slate-800 rounded-2xl p-4"
                            >

                                <div className="flex items-center gap-4 min-w-0">

                                    <FileText
                                        className="text-cyan-400 shrink-0"
                                        size={22}
                                    />

                                    <span className="text-white truncate">
                                        {filename}
                                    </span>

                                </div>

                                <button
                                    onClick={() => handleDelete(filename)}
                                    className="text-slate-400 hover:text-red-400 transition"
                                >
                                    <Trash2 size={20} />
                                </button>

                            </div>

                        ))}

                    </div>

                )}

            </div>

            {/* Extracted Text */}

            <div className="bg-slate-900 border border-slate-700 rounded-3xl p-6">

                <div className="flex items-center gap-3 mb-5">

                    <CheckCircle2
                        className="text-green-400"
                        size={22}
                    />

                    <h2 className="text-2xl font-bold text-white">
                        Extracted Text
                    </h2>

                </div>

                <div className="bg-slate-950 rounded-2xl p-5 min-h-[180px] max-h-[400px] overflow-y-auto">

                    {pdfText ? (

                        <pre className="text-slate-300 whitespace-pre-wrap font-sans leading-7">
                            {pdfText}
                        </pre>

                    ) : (

                        <p className="text-slate-600">
                            Extracted PDF text will appear here.
                        </p>

                    )}

                </div>

            </div>

        </div>
    );
}