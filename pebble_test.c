#include <pebble.h>

static Window *s_main_window;
static TextLayer *s_status_layer;
static void inbox_received_callback(DictionaryIterator *iterator, void *context)
{
   Tuple *tuple = dict_find(iterator,MESSAGE_KEY_SLEEPING);
  
  if(tuple)
  {
    if( tuple -> value ->int32)
    {
      text_layer_set_text(s_status_layer, "Wake up!!!");
      text_layer_set_background_color(s_status_layer, GColorRed);
      vibes_long_pulse();
    }else
    {
      text_layer_set_text(s_status_layer, "Good job!!!");  
      text_layer_set_background_color(s_status_layer, GColorGreen);
    }
  }
  
  
}
static void main_window_load(Window *window)
{
  Layer *window_layer = window_get_root_layer(window);
  GRect bounds = layer_get_bounds(window_layer);
  
  // Create temperature Layer
  s_status_layer = text_layer_create(
  GRect(0, PBL_IF_ROUND_ELSE(58, 52), bounds.size.w, 50));

  // Style the text
  text_layer_set_background_color(s_status_layer, GColorCyan);
  text_layer_set_text_color(s_status_layer, GColorWhite);
  text_layer_set_text_alignment(s_status_layer, GTextAlignmentCenter);
  text_layer_set_text(s_status_layer, "Loading");
  text_layer_set_font(s_status_layer, fonts_get_system_font(FONT_KEY_GOTHIC_28));
  
  layer_add_child(window_layer, text_layer_get_layer(s_status_layer));
}

static void main_window_unload(Window *window)
{
   text_layer_destroy(s_status_layer);
}

static void init()
{
  //messenging 
  app_message_register_inbox_received(inbox_received_callback);
  const int inbox_size = 128;
  const int outbox_size = 128;
  app_message_open(inbox_size, outbox_size);
  
  s_main_window = window_create();
  
  window_set_window_handlers(s_main_window, (WindowHandlers)
                            {
                              .load = main_window_load,
                              .unload = main_window_unload
                            });
  window_stack_push(s_main_window, true);
}

static void deinit()
{
  window_destroy(s_main_window);
}

int main(void)
{
  init();
  app_event_loop();
  deinit();
}
