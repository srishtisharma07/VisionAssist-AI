import Header from "./components/Header";
import WebcamPanel from "./components/WebcamPanel";
import ChatPanel from "./components/ChatPanel";
import PDFUploadPanel from "./components/PDFUploadPanel";
import AssistantStatus from "./components/AssistantStatus";

function App() {

    return (

        <div className="min-h-screen bg-slate-900">

            <Header />

            <div className="max-w-7xl mx-auto p-6 space-y-6">

                <div className="grid grid-cols-3 gap-6">

                    <div className="space-y-6">

                        <WebcamPanel />

                        <AssistantStatus />

                    </div>

                    <div className="col-span-2">

                        <ChatPanel />

                    </div>

                </div>

                <PDFUploadPanel />

            </div>

        </div>

    );

}

export default App;