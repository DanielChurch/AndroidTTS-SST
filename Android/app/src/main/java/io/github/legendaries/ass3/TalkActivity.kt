package io.github.legendaries.ass3

import android.app.Activity
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.Button
import android.widget.EditText
import android.speech.RecognizerIntent
import android.content.Intent
import android.widget.TextView

class TalkActivity: AppCompatActivity() {
    private val REQUEST_CODE = 69

    override fun onCreate(savedInstance: Bundle?) {
        super.onCreate(savedInstance)
        setContentView(R.layout.tts_activity)

        val editText = findViewById<EditText>(R.id.tts_text).apply {
            setText(context.getString(R.string.voiceline1))
        }

        val tts = TTS(this).apply { start() }

        findViewById<Button>(R.id.tts_button).run {
            setOnClickListener {
                speakText(tts, editText.text.toString())
            }
        }

        findViewById<Button>(R.id.stt_button).run {
            setOnClickListener {
                listenForSpeech()
            }
        }
    }

    private fun listenForSpeech() {
        startActivityForResult(
                Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
                    putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
                }, REQUEST_CODE
        )
    }

    private fun speakText(tts: TTS, text: String) {
        tts.handler.run {
            sendMessage(
                obtainMessage().apply {
                    data = Bundle().apply {
                        putString("TT", text)
                    }
                }
            )
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent) {
        if (requestCode == REQUEST_CODE && resultCode == Activity.RESULT_OK) {
            data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS).let {
//                SocketConnection(this, intent.getStringExtra("ip"), intent.getStringExtra("port").toInt(), it.joinToString(" "))
                findViewById<TextView>(R.id.status).text = it.joinToString(" ")
            }
        }
        super.onActivityResult(requestCode, resultCode, data)
    }
}