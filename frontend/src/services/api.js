const BASE_URL = "http://127.0.0.1:8000";

export async function sendCommand(command) {
    try {
        const response = await fetch(
            `${BASE_URL}/agent?command=${encodeURIComponent(command)}`
        );

        return await response.json();

    } catch (error) {
        console.error(error);

        return {
            response: "Unable to connect to backend."
        };
    }
}

export async function uploadPDF(file) {

    const formData = new FormData();
    formData.append("file", file);

    try {

        const response = await fetch(
            `${BASE_URL}/pdf/upload`,
            {
                method: "POST",
                body: formData,
            }
        );

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));

            throw new Error(
                errorData.detail || `Server returned ${response.status}`
            );
        }

        return await response.json();

    } catch (error) {

        console.error("Upload Error:", error);

        return {
            success: false,
            message: error.message,
        };
    }
}

export async function getAssistantState() {

    try {

        const response = await fetch(
            `${BASE_URL}/state`
        );

        return await response.json();

    } catch (error) {

        console.error("State Error:", error);

        return {};

    }
}

export async function getPdfInfo() {

    try {

        const response = await fetch(
            `${BASE_URL}/pdf/info`
        );

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        return await response.json();

    } catch (error) {

        console.error("PDF Info Error:", error);

        return {
            total_pdfs: 0,
            uploaded_pdfs: [],
            characters: 0,
        };
    }
}

export async function getPdfText() {

    try {

        const response = await fetch(
            `${BASE_URL}/pdf/text`
        );

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        return await response.json();

    } catch (error) {

        console.error("PDF Text Error:", error);

        return {
            text: "",
        };
    }
}

export async function deletePdf(filename) {

    try {

        const response = await fetch(
            `${BASE_URL}/pdf/${encodeURIComponent(filename)}`,
            {
                method: "DELETE",
            }
        );

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        return await response.json();

    } catch (error) {

        console.error("Delete PDF Error:", error);

        return {
            success: false,
            message: error.message,
        };
    }
}

export async function clearAllPdfs() {

    try {

        const response = await fetch(
            `${BASE_URL}/pdf/clear`,
            {
                method: "DELETE",
            }
        );

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        return await response.json();

    } catch (error) {

        console.error("Clear PDFs Error:", error);

        return {
            success: false,
            message: error.message,
        };
    }
}