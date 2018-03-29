package io.github.legendaries.ass3

import android.annotation.SuppressLint
import android.app.Activity
import android.os.Build
import android.os.Handler
import android.os.Looper
import android.os.Message
import android.speech.tts.TextToSpeech
import java.util.*

class TTS (activity: Activity): Thread(), TextToSpeech.OnInitListener {
    val tts = TextToSpeech(activity, this)

    lateinit var handler: Handler

    override fun onInit(status: Int) {
        if (status != TextToSpeech.SUCCESS) return

        tts.run {
            language = Locale.US
            setPitch(0f)
            setSpeechRate(0f)
        }
    }

    override fun run() {
        Looper.prepare()

        handler = @SuppressLint("HandlerLeak")
        object: Handler() {
            override fun handleMessage(msg: Message?) {
                super.handleMessage(msg)

                msg?.data?.getString("TT")?.let { speak(it) }
            }
        }

        Looper.loop()
    }

    fun speak(text: String) {
        when {
            Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP -> tts.speak(text, TextToSpeech.QUEUE_FLUSH, null, null)
            else -> tts.speak(text, TextToSpeech.QUEUE_FLUSH, null)
        }

        while (tts.isSpeaking) {
            try {
                Thread.sleep(200)
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }
}