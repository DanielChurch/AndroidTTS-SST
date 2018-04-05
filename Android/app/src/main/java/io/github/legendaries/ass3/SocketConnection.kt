package io.github.legendaries.ass3

import android.annotation.SuppressLint
import android.app.Activity
import android.os.Handler
import android.os.Looper
import android.os.Message
import android.util.Log
import java.io.DataInputStream
import java.io.PrintWriter
import java.net.Socket

class SocketConnection(val parent: TalkActivity, val ip: String, val port: Int): Thread() {
    lateinit var socket: Socket

    lateinit var handler: Handler

    var init = false;

    override fun run() {
        super.run()

        if (!init) {
            socket = Socket(ip, port)
            init = true
        }

        Looper.prepare()

        // Handle STT send data back to Python
        handler = @SuppressLint("HandlerLeak")
        object: Handler() {
            override fun handleMessage(msg: Message?) {
                super.handleMessage(msg)

                Log.v("Android", "We made it boiiis")

                msg?.data?.getString("TT")?.let {
                    writeMessage(it)
                }
            }
        }

        // Handle reading from the server
        // readMessage()

        Looper.loop()
    }

    private fun readMessage() {
        val dis = DataInputStream(socket.getInputStream())
        try {
            val value = dis.readUTF()

            // Server can request tts or sst
            when (value.split(" ")[0]) {
            // Speak the network params if tts
                "tts" -> parent.speakText(value.split(" ").subList(1, value.split(" ").size - 1).joinToString(" "))
            // Send the listened text to the server
                "sst" -> parent.listenForSpeech()
                else -> {}
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    private fun writeMessage(message: String) {
        socket.let {
            try {
                PrintWriter(it.getOutputStream(), true).use {
                    it.run {
                        Log.v("Android", message)
                        print(message)
                        flush()
                    }
                }
            } catch (e: Throwable) {
                e.printStackTrace()
            }
        }
    }
}
