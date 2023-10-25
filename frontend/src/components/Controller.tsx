import { useState } from "react"
import Title from "./Title"
import RecordMessage from "./RecordMessage"
import axios from "axios"

function Controller() {
    const [isLoading, setIsLoading] = useState(false)
    const [messages, setMessages] = useState<any[]>([])


    // functions
    const createBlobUrl = (data: any) => {
        const blob = new Blob([data], { type: "audio/wav" })
        const url = window.URL.createObjectURL(blob)        //this is passed as the octet stream
        return url
    }

    const handleStop = async (blobUrl: string) => {
        setIsLoading(true)

        // appending recorded message to messages
        const myMessage = { sender: "me", blobUrl }
        const messagesArr = [...messages, myMessage]       //adding my message to the spread of messages
        
        //convert blob url to blob object 
        fetch(blobUrl)
            .then((res) => res.blob())
            .then(async (blob) => {
                //construct audio to send file
                const formData = new FormData()
                formData.append("file", blob, "myFile.wav") //pulling from the wave file in the backend file path
                //send form data to API endpoint
                await axios.post("http://localhost:8000/post-audio", formData, {
                    headers: {"Content-Type": "audio/mpeg" }, 
                    responseType: "arraybuffer",
                }).then((res: any) => {
                    const blob = res.data
                    const audio = new Audio()
                    audio.src = createBlobUrl(blob)
                    //append to audio
                    const botMessage = {sender: "bot", blobUrl: audio.src}
                    messagesArr.push(botMessage)
                    setMessages(messagesArr)

                    //auto play audio
                    setIsLoading(false)
                    audio.play()
                }).catch((err) => {
                    console.error(err.message)
                    setIsLoading(false)
                })
            })
        setIsLoading(false)
    }

    return (
        <div className="h-screen overflow-y-hidden">
            <Title setMessages={setMessages}/>
            <div className="flex flex-col justify-between h-fill overflow-y-scroll pb-96">
                {/* recorder */}
                <div className="fixed bottom-0 w-full py-6 border-t text-center bg-gradient-to-r from-sky-500 to-green-500">
                    <div className="flex justify-center items-center w-full">
                        <div>
                            <RecordMessage handleStop={handleStop} />
                        </div>
                    </div>
                </div>
            </div>
        </div>
  )
}

export default Controller