import os

filepath = "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo2.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

corrupted_part = """                                <div class="tab-pane fade" id="semana8" role="tabpanel" aria-labelledby="semana8-tab">
                                     <div class="card-body">
                                         <p style="text-align: justify;">Elabore el documento: <strong>caso Ismael
                                                 rel="noopener"><button type="button"
                                                     class="btn btn-outline-primary btn-lg" aria-pressed="true"
                                                     role="button"> <span class="spinner-grow spinner-grow-sm"></span>
                                                     Enviar Entregable 3. </button></a>
                                         </div>
                                     </div>
                                 </div>"""

# Let's verify if we can find a simpler substring to match and replace, in case whitespace differs
target_start = 'id="semana8"'
target_end = 'id="semana9"'

idx_start = content.find(target_start)
idx_end = content.find(target_end)

if idx_start != -1 and idx_end != -1:
    # Find the <div class="tab-pane... before id="semana8"
    div_start = content.rfind("<div", 0, idx_start)
    # Find the <div class="tab-pane... before id="semana9"
    div_next = content.rfind("<div", 0, idx_end)
    
    print(f"Indices: div_start={div_start}, div_next={div_next}")
    
    restored_semana8 = """<div class="tab-pane fade" id="semana8" role="tabpanel" aria-labelledby="semana8-tab">
                                     <div class="card-body">
                                         <p style="text-align: justify;">Elabore el documento: <strong>caso Ismael Bukowsky: micro relatos de vigorexia y depravación</strong>, teniendo en cuenta la siguiente estructura:</p>
                                         <br><br>
                                         <ul>
                                             <li>Portada.</li>
                                             <li>Introducción.</li>
                                             <li>Cuerpo del trabajo: desarrollo. caso Ismael Bukowsky: micro relatos de vigorexia y depravación.</li>
                                             <li>Conclusiones.</li>
                                             <li>Bibliografía.</li>
                                         </ul>
                                         <br><br>
                                         <p style="text-align: justify;">Envíe el documento en formato PDF en las fechas establecidas.</p>
                                         <br>
                                         <div style="text-align: center;">
                                             <a target="_blank" href="https://virtual.udes.edu.co/mod/assign/view.php?id=3893" rel="noopener">
                                                 <button type="button" class="btn btn-outline-primary btn-lg" aria-pressed="true" role="button">
                                                     <span class="spinner-grow spinner-grow-sm"></span> Enviar Entregable 3.
                                                 </button>
                                             </a>
                                         </div>
                                     </div>
                                 </div>
                                 """
    
    new_content = content[:div_start] + restored_semana8 + content[div_next:]
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Success: week 8 restored.")
else:
    print("Error: week 8 indices not found.")
