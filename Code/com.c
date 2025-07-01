#include <gtk/gtk.h>
#include <espeak-ng/speak_lib.h>
#include <opencv2/opencv.hpp>
#include <pocketsphinx.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to handle text-to-speech
void speak_text(const char *text) {
    char command[256];
    snprintf(command, sizeof(command), "espeak '%s'", text);
    system(command);
}

// Function to recognize speech (dummy function for now)
void recognize_speech(GtkTextBuffer *buffer) {
    GtkTextIter iter;
    gtk_text_buffer_get_end_iter(buffer, &iter);
    gtk_text_buffer_insert(buffer, &iter, "Blind: Recognized speech\n", -1);
}

// Function to send text input to conversation area
void send_text(GtkWidget *entry, GtkTextBuffer *buffer) {
    const char *text = gtk_entry_get_text(GTK_ENTRY(entry));
    GtkTextIter iter;
    gtk_text_buffer_get_end_iter(buffer, &iter);
    gtk_text_buffer_insert(buffer, &iter, "Deaf/Mute: ", -1);
    gtk_text_buffer_insert(buffer, &iter, text, -1);
    gtk_text_buffer_insert(buffer, &iter, "\n", -1);
    speak_text(text);
    gtk_entry_set_text(GTK_ENTRY(entry), "");
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);
    
    GtkWidget *window, *vbox, *entry, *send_button, *text_view, *scroll;
    GtkTextBuffer *buffer;
    
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Communication System");
    gtk_container_set_border_width(GTK_CONTAINER(window), 10);
    gtk_widget_set_size_request(window, 400, 500);
    
    vbox = gtk_vbox_new(FALSE, 5);
    gtk_container_add(GTK_CONTAINER(window), vbox);
    
    text_view = gtk_text_view_new();
    buffer = gtk_text_view_get_buffer(GTK_TEXT_VIEW(text_view));
    gtk_text_view_set_editable(GTK_TEXT_VIEW(text_view), FALSE);
    
    scroll = gtk_scrolled_window_new(NULL, NULL);
    gtk_container_add(GTK_CONTAINER(scroll), text_view);
    gtk_box_pack_start(GTK_BOX(vbox), scroll, TRUE, TRUE, 0);
    
    entry = gtk_entry_new();
    gtk_box_pack_start(GTK_BOX(vbox), entry, FALSE, FALSE, 0);
    
    send_button = gtk_button_new_with_label("Send");
    g_signal_connect(send_button, "clicked", G_CALLBACK(send_text), entry);
    gtk_box_pack_start(GTK_BOX(vbox), send_button, FALSE, FALSE, 0);
    
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);
    
    gtk_widget_show_all(window);
    gtk_main();
    
    return 0;
}
