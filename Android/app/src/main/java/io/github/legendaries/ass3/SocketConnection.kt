package io.github.legendaries.ass3

import android.app.Activity
import java.io.PrintWriter
import java.net.Socket

class SocketConnection(val parent: Activity, val ip: String, val port: Int, val message: String): Thread() {
    val socket = Socket(ip, port)

    override fun run() {
        super.run()

        parent.runOnUiThread {

        }

        writeMessage()
    }

    private fun writeMessage() {
        socket.let {
            try {
                PrintWriter(it.getOutputStream(), true).use {
                    it.run {
                        println(message.toByteArray())
                        flush()
                    }
                }
            } catch (e: Throwable) {
                e.printStackTrace()
            }
        }
    }
}
