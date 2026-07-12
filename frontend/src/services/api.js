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

        console.log("Status:", response.status);

        if (!response.ok) {
            throw new Error("Server returned " + response.status);
        }

        const data = await response.json();

        console.log("Backend Response:", data);

        return data;

    } catch (error) {

        console.error("Upload Error:", error);

        return {
            success: false,
            message: error.message
        };
    }
}

export async function getAssistantState() {

    try {

        const response = await fetch(`${BASE_URL}/state`);

        return await response.json();

    } catch (error) {

        console.error(error);

        return {};

    }
}